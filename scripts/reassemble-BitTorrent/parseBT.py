packets = list()

f = open('packets')
data = f.read()
f.close()

for line in data.split('\n'):
    values = line.split('\t')
    if(len(values)==2):
        indexes = values[0].split(',')
        datas = values[1].split(',')
        for idx in range(0, len(indexes)):
            packets.append({'idx': indexes[idx], 'data': datas[idx]})

packets = sorted(packets, key=lambda packet: packet['idx'])

f = open('torrent_out.bin', 'wb')

for packet in packets:
    temp = packet['data'].split(":")
    temp[0] = temp[0].strip()
    f.write(''.join(temp[0].decode('hex')))

f.close()
