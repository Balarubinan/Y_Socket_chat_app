from src.multi_client import CustomPlayer
ply1=CustomPlayer('127.0.0.1',5000)
ply1.connect_to_host()
ply1.start_recv()