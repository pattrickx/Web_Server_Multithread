import os

def process_message(server_folder,message):
    query_dict = {}
    query_list = message.split("\r\n")
    query_dict['command'], query_dict['path'], query_dict['protocol'] = query_list[0].split(" ")
    query_dict['msg']=message.split("\r\n\r\n")[1] if len(message.split("\r\n\r\n"))==2 else ''
    if query_dict['path'] == "/":
        query_dict['path'] = server_folder + '/index.html'
    else:
        query_dict['path'] = server_folder + query_dict['path']
    query_dict['path'] = query_dict['path'] + '' if 'index.html' in query_dict['path'] else '/index.html'
    # query_dict['Host'] = query_list[1].split("")[1]
    # query_dict['Connection'] = query_list[2].split("")[1]
    return query_dict