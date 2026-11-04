import json
from channels.generic.websocket import AsyncWebsocketConsumer


class KDSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('kds', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('kds', self.channel_name)

    async def receive(self, text_data):
        pass

    async def order_update(self, event):
        await self.send(text_data=json.dumps(event['data']))
