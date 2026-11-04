import jwt
import datetime
from django.conf import settings
from tenants.models import License, Subscription, Tenant


class LicenseManager:
    @staticmethod
    def generate_license(tenant, max_branches=1, max_users=10, days=365):
        payload = {
            'tenant_id': tenant.id,
            'slug': tenant.slug,
            'max_branches': max_branches,
            'max_users': max_users,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=days),
            'iat': datetime.datetime.utcnow()
        }
        key = getattr(settings, 'LICENSE_PRIVATE_KEY', settings.SECRET_KEY)
        token = jwt.encode(payload, key, algorithm='HS256')
        license = License.objects.create(
            tenant=tenant,
            license_key=token,
            expires_at=payload['exp'],
            max_branches=max_branches,
            max_users=max_users,
            status='active'
        )
        return license

    @staticmethod
    def validate_license(license_key):
        try:
            key = getattr(settings, 'LICENSE_PUBLIC_KEY', getattr(settings, 'LICENSE_PRIVATE_KEY', settings.SECRET_KEY))
            payload = jwt.decode(license_key, key, algorithms=['HS256'])
            license = License.objects.filter(license_key=license_key, status='active').first()
            if not license:
                return {'valid': False, 'error': 'License not found'}
            if license.expires_at and license.expires_at < datetime.datetime.now(datetime.timezone.utc):
                return {'valid': False, 'error': 'License expired'}
            return {'valid': True, 'license': license, 'payload': payload}
        except jwt.ExpiredSignatureError:
            return {'valid': False, 'error': 'License expired'}
        except Exception as e:
            return {'valid': False, 'error': str(e)}
