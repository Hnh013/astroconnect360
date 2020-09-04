import json
###
import datetime
###
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class Consumer(WebsocketConsumer):
############################ joining chat ####################################333
    def connect(self):
        self.person_name=self.scope['url_route']['kwargs']['person_name']
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name='chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":self.person_name+" Joined Chat"
            }
        )
        self.accept()

        ############### making entry in db
        

###############################  Leaving chat #############################

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":self.person_name+" Left Chat"
            }
        )
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

        ####################### making entry in db
        
################################# receiving a tpyed message ##################3
    def receive(self, text_data=None, bytes_data=None):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':self.person_name+" : "+message
            }
        )

        ###################### saving message
        

################################################## sending message


    def chat_message(self,event):
        message=event['message']

        self.send(text_data=json.dumps({
            'message':message
        }))
        