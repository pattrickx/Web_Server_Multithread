import os

def process_message(server_folder,message):
    query_dict = {}
    query_list = message.split("\r\n")
    if len(query_list[0].split(" "))==3:
        query_dict['command'], query_dict['path'], query_dict['protocol'] = query_list[0].split(" ")
        msg = message.split("\r\n\r\n")
        query_dict['msg']=msg[1] if len(msg)==2 else ''
        if "Connection:" in message:
            query_dict["connection"]= ((message.split("Connection:"))[1].split("\r\n"))[0]
        else:
            query_dict["Connection"]=""
        if query_dict['path'] == "/":
            query_dict['path'] = server_folder + '/index.html'
        else:
            query_dict['path'] = server_folder + query_dict['path']
        query_dict['path'] = query_dict['path'] + '' if '.' in query_dict['path'] else '/index.html'
        # query_dict['Host'] = query_list[1].split("")[1]
        # query_dict['Connection'] = query_list[2].split("")[1]
    return query_dict