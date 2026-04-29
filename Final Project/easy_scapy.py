"""
Easy Scapy: A Beginner-Friendly Network Security Toolkit

This program provides a graphical interface for performing basic network
security tasks using Scapy. It allows users to create and send custom packets,
capture and filter live network traffic, and perform traceroute operations.
"""

from scapy.all import *    # Scapy provides packet creation, sending, and sniffing functionality
import ipaddress           # ipaddress is used to validate user-entered IP addresses
import easygui             # easygui provides a simple GUI for user interaction
import socket              # socket is used to resolve domain names to IP addresses

# -------------------------
# PACKET CLASS
# -------------------------

class Packet:
    def __init__(self):
        """Class responsible for creating and sending custom packets"""

    def user_menu(self):
        """Collect user input for packet creation (type, TTL, addresses, payload) and ensure input is valid"""
        valid_input = "n"
        # Prompt user to select packet protocol (ICMP, TCP, UDP)
        while valid_input == "n":
            packet_type = easygui.buttonbox("Choose a packet type", "Packet Creator", ["ICMP", "TCP", "UDP"])
            if packet_type == None:
                easygui.msgbox("Please choose a packet type")
            else:
                break
        # Get and validate TTL value (must be integer between 0–255)
        while valid_input == "n":
            ttl = easygui.enterbox("Enter packet TTL: ", "Packet Creator")
            if ttl == None:
                easygui.msgbox("Please enter an integer 0-255")
                continue
            try:
                int_ttl = int(ttl)
                if int_ttl < 0 or int_ttl > 255:
                    easygui.msgbox("Please enter an integer 0-255")
                else:
                    break
            except ValueError:
                easygui.msgbox("Please enter an integer 0-255")
        # Get and validate source IP address
        while valid_input == "n":
            source_address = easygui.enterbox("Enter source IP address: ", "Packet Creator")
            if source_address == None:
                easygui.msgbox("Please enter a valid IP address")
                continue
            try:
                ipaddress.ip_address(source_address)
                break
            except ValueError:
                easygui.msgbox("Please enter a valid IP address")
        # Get destination (accepts IP or domain name and resolves if needed)
        while valid_input == "n":
            destination_address = easygui.enterbox("Enter destination IP address or domain name: ", "Packet Creator")
            if destination_address == None:
                easygui.msgbox("Please enter a valid IP address or domain name")
                continue
            try:
                ipaddress.ip_address(destination_address)
                break
            except ValueError:
                try:
                    destination_address = socket.gethostbyname(destination_address)
                    break
                except:
                    easygui.msgbox("Please enter a valid IP address or domain name")
        # Optional payload data to include in packet
        raw_data = easygui.enterbox("Enter packet raw data: ", "Packet Creator")
        # Pass validated inputs to create_packet function
        self.create_packet(packet_type, int_ttl, source_address, destination_address, raw_data)

    def create_packet(self, packet_type, ttl, src_addr, dst_addr, raw_data):
        """Build packet based on selected parameters"""
        # Set protocol
        if packet_type == "ICMP":
            packet = IP()/ICMP()
        elif packet_type == "TCP":
            packet = IP()/TCP()
        elif packet_type == "UDP":
            packet = IP()/UDP()
        # Attach raw payload if provided by user
        if raw_data:
            packet = packet / raw_data
        # Set IP header fields (source, destination, TTL)
        packet.src = src_addr
        packet.dst = dst_addr
        packet.ttl = ttl
        # Pass the created packet into the send_packet function
        self.send_packet(packet)


    def send_packet(self, packet):
        """Display packet information, confirm with user, and send packet"""
        # Display packet information to user and confirm before sending
        packet_info = packet.show(dump=True)
        packet_send = easygui.ynbox(f"Send Packet?\n\n{packet_info}", "Packet Creator")
        if packet_send == True:
            # Send packet using scapy
            send(packet)
            easygui.msgbox("Packet sent!", "Packet Creator")
        else:
            easygui.msgbox("Packet cancelled", "Packet Creator")

# -------------------------
# SNIFFER CLASS
# -------------------------

class Sniffer:
    def __init__(self):
        """Class responsible for capturing and optionally saving network traffic"""
        self.file_name = ""
        self.pcap_writer = None

    def user_menu(self):
        """Collect and validate user input for sniffing (count, filters, saving)"""
        valid_input = "n"
        # Get number of packets to capture
        while valid_input == "n":
            number = easygui.enterbox("How many packets would you like to sniff?", "Packet Creator")
            if number == None:
                easygui.msgbox("Please choose a valid packet number")
            else:
                try:
                    number = int(number)
                    if number < 1:
                        easygui.msgbox("Please choose a valid packet number")
                    else:
                        break
                except ValueError:
                    easygui.msgbox("Please choose a valid packet number")
        # Let user choose filtering options
        choices = easygui.multchoicebox("Filter by:", "Sniffer", ["Port", "Protocol", "Host address", "Destination address"])
        if choices == None:
            choices = []
        # Get and validate port filter (0–65535)
        if "Port" in choices:
            while valid_input == "n":
                port = easygui.enterbox("Enter port: ", "Sniffer")
                if port == None:
                    easygui.msgbox("Please enter a valid port number")
                else:
                    try:
                        port = int(port)
                        if port < 0 or port > 65535:

                            continue
                        else:
                            break
                    except ValueError:
                        easygui.msgbox("Please enter a valid port number")
        else:
            port = None
        # Select protocol filter (ICMP, TCP, UDP)
        if "Protocol" in choices:
            while valid_input == "n":
                protocol = easygui.buttonbox("Choose protocol", "Sniffer", ["ICMP", "TCP", "UDP"])
                if protocol == None:
                    easygui.msgbox("Please choose a protocol")
                else:
                    break
        else:
            protocol = None
        # Get and validate source host IP filter
        if "Host address" in choices:
            while valid_input == "n":
                host = easygui.enterbox("Enter host address: ", "Sniffer")
                if host == None:
                    easygui.msgbox("Please enter a valid host address")
                    continue
                try:
                    ipaddress.ip_address(host)
                    break
                except ValueError:
                    easygui.msgbox("Please enter a valid host address")
        else:
            host = None
        # Get destination filter (IP or domain name)
        if "Destination address" in choices:
            while valid_input == "n":
                destination = easygui.enterbox("Enter destination address or domain name: ", "Sniffer")
                if destination == None:
                    easygui.msgbox("Please enter a valid destination address or domain name")
                    continue
                try:
                    ipaddress.ip_address(destination)
                    break
                except ValueError:
                    try:
                        destination = socket.gethostbyname(destination)
                        break
                    except:
                        easygui.msgbox("Please enter a valid IP address or domain name")
        else:
            destination = None
        # Reset file_name variable in case this is not the first sniff
        self.file_name = ""
        # Ask user if captured packets should be saved to a file
        if easygui.ynbox("Save packets to a file?", "Sniffer"):
            # Validate filename and initialize PCAP writer
            while valid_input == "n":
                self.file_name = easygui.enterbox("Enter file name with a .pcap extension: ", "Sniffer")
                try:
                    if not self.file_name.endswith(".pcap"):
                        easygui.msgbox("Please enter a valid file name with a .pcap extension")
                    else:
                        self.pcap_writer = PcapWriter(self.file_name, append=True, sync=True)
                        break
                except:
                    easygui.msgbox("Please enter a valid file name with a .pcap extension")
        # Call sniffer function with parameters (number, port, protocol, host, destination)
        self.sniffer(number, port, protocol, host, destination)

    def sniffer(self, number, port, protocol, host, destination):
        """Build filter string based on user input and start packet capture"""
        # Build BPF (Berkeley Packet Filter) string based on user input
        filter1 = ""
        if protocol != None:
            filter1 += f"{protocol.lower()}"
        if host != None:
            if filter1 == "":
                filter1 += f"host {host}"
            else:
                filter1 += f" and host {host}"
        if destination != None:
            if filter1 == "":
                filter1 += f"dst host {destination}"
            else:
                filter1 += f" and dst host {destination}"
        if port != None:
            if filter1 == "":
                filter1 += f"port {port}"
            else:
                filter1 += f" and port {port}"
        print(filter1)
        try:
            # Start packet capture with filter and callback function
            sniff(filter=filter1, prn=self.packet_callback, count=number)
            # Notify user when sniffing is complete
            easygui.msgbox("Sniff complete (output in terminal)", "Sniffer")
            if self.file_name != "":
                easygui.msgbox(f"Packets saved to {self.file_name}", "Sniffer")
        except:
            # Handle invalid filter expressions
            easygui.msgbox("Cannot set filter, expression rejects all packets")

    def packet_callback(self, packet):
        """Processes, displays, and saves (if enabled) sniffed packets"""
        # Display packet details in terminal
        print(packet.show())
        # Save packet to file if saving is enabled
        if self.file_name != "":
            self.pcap_writer.write(packet)

# -------------------------
# TRACE_ROUTE CLASS
# -------------------------

class Traceroute:
    def __init__(self):
        """Class used to perform traceroute using ICMP packets"""

    def user_menu(self):
        """Get destination for traceroute from user (IP or domain name)"""
        valid_input = "n"
        while valid_input == "n":
            destination = easygui.enterbox("Enter destination address or domain name:", "Traceroute")
            if destination == None:
                easygui.msgbox("Please enter a valid destination address or domain name")
                continue
            try:
                ipaddress.ip_address(destination)
                break
            except ValueError:
                try:
                    destination = socket.gethostbyname(destination)
                    break
                except:
                    easygui.msgbox("Please enter a valid IP address or domain name")
        self.start(destination)

    def start(self, destination):
        """Perform traceroute by incrementing TTL values"""
        print(f"Traceroute to {destination} in a maximum of 30 hops")
        # Send packets with increasing TTL to discover each hop
        for ttl in range(1, 31):
            packet = IP(dst=destination, ttl=ttl) / ICMP()
            # Send packet and wait for a single reply
            reply = sr1(packet, verbose=0, timeout=2)
            if reply is None:
                # No response received within timeout
                print(f"{ttl} * * *")
            elif reply.type == 0:
                # Reached destination (ICMP Echo Reply)
                print(f"{ttl} {reply.src} (Target Reached)")
                break
            else:
                # Intermediate hop (ICMP Time Exceeded)
                print(f"{ttl} {reply.src}")
        print()
        easygui.msgbox("Traceroute complete (output in terminal)", "Traceroute")

# -------------------------
# PROGRAM START
# -------------------------

# Initialize objects for each tool (packet sender, sniffer, traceroute)
packet1 = Packet()
sniff1 = Sniffer()
traceroute1 = Traceroute()

# Main menu loop for user interaction
while True:
    choice = easygui.buttonbox("Welcome to easy Scapy!", "Easy Scapy", ["Send Packet", "Sniff Traffic", "Traceroute", "Quit"])
    if choice == "Send Packet":
        packet1.user_menu()
    if choice == "Sniff Traffic":
        sniff1.user_menu()
    if choice == "Traceroute":
        traceroute1.user_menu()
    if choice == "Quit":
        break
    if choice == None:
        break