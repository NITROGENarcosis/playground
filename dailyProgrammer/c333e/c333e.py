from sys import stdin

class Packet:
    def __init__(self):
        self.pid = 0
        self.numFrags = 0
        self.frags = dict()

    def __str__(self) :
        output = ""
        for x in iter(self.frags) :
            output = output + str(self.pid) + "\t" + str(x) + "\t"
            output = output + str(self.numFrags) + "\t" + self.frags[x] + "\n"
        return output


packets = dict()
for line in iter(stdin.readline, '') :
    #split the line up
    lineParts = line.split()
    #assign parts names
    pid = int(lineParts[0])
    fragId = int(lineParts[1])
    fragCount = int(lineParts[2])
    text = ""
    #check for blank lines
    if len(lineParts) < 4 :
        text = " "
    else:
        text = " ".join( lineParts[3:] )

    #check if a new packet id or existing
    if pid not in packets :
        #add new packet
        packet = Packet()
        packet.pid = pid
        packet.numFrags = fragCount
        packets[pid] = packet

    #add the frag to the packet
    packet = packets[pid]
    packet.frags[fragId] = text

    #check if packet is complete and if so print it and remove it
    toBeDel = []
    for pid in packets.keys():
        p = packets[pid]
        if len(p.frags) == p.numFrags:
            print( p,end="" )
            toBeDel.append(pid)
    for pid in toBeDel:
        del packets[pid]
