from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification, DeviceToken


class NotificationService:
    @staticmethod
    def send_notification(tenant, title, message, type='system', user=None, data=None):
        notification = Notification.objects.create(
            tenant=tenant,
            user=user,
            title=title,
            message=message,
            type=type,
            data=data or {}
        )
        
        channel_layer = get_channel_layer()
        if channel_layer:
            group = f'notifications_{tenant.id}'
            if user:
                group = f'notifications_{tenant.id}_{user.id}'
            async_to_sync(channel_layer.group_send)(
                group,
                {
                    'type': 'send_notification',
                    'notification': {
                        'id': notification.id,
                        'title': title,
                        'message': message,
                        'type': type,
                        'data': data or {}
                    }
                }
            )
        return notification

    @staticmethod
    def notify_new_order(tenant, order):
        NotificationService.send_notification(
            tenant=tenant,
            title='New Order',
            message=f'Order #{order.order_no} received',
            type='order',
            data={'order_id': order.id, 'order_no': order.order_no}
        )

    @staticmethod
    def notify_kds_update(tenant, order, status):
        NotificationService.send_notification(
            tenant=tenant,
            title='Order Update',
            message=f'Order #{order.order_no} - {status}',
            type='kds',
            data={'order_id': order.id, 'status': status}
        )
