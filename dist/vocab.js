const vocabRows = `1|Layering|Dividing network communication into levels with distinct responsibilities, so each can change with less impact on others.
1|Protocol|An agreed set of rules for communication between systems.
1|TCP/IP|Transmission Control Protocol / Internet Protocol|The Internet protocol suite; this course uses the five-layer teaching model.
1|Application layer|Provides network services to user applications.
1|Transport layer|Provides communication between application processes on end hosts.
1|Network layer|Handles logical IP addressing and routing packets between networks.
1|Data Link layer|Moves frames over a local link using link-layer addresses.
1|Physical layer|Transmits bits as electrical, optical or radio signals.
1|OSI|Open Systems Interconnection|A seven-layer networking reference model.
1|Presentation layer|Represents data formats and can provide compression and encryption.
1|Session layer|Establishes, manages and ends communication sessions.
1|Encapsulation|Adding protocol control information as data moves down a stack.
1|Decapsulation|Removing protocol control information as data moves up a stack.
1|IEEE|Institute of Electrical and Electronics Engineers|Develops standards including Ethernet and wireless LAN standards.
1|IETF|Internet Engineering Task Force|Develops Internet technical standards and protocols.
1|LAN|Local Area Network|A network covering a limited area such as a building.
1|WLAN|Wireless Local Area Network|A local-area network using wireless communication.
1|TCP|Transmission Control Protocol|A transport protocol providing reliable, ordered byte-stream delivery.
1|IP|Internet Protocol|A network-layer protocol that addresses and routes packets.
1|DNS|Domain Name System|A distributed system that maps names to records such as IP addresses.
1|HTTP|Hypertext Transfer Protocol|An application protocol used to exchange web resources.
1|Interoperability|The ability of different systems or products to work together.
2|Physical medium|The material or environment through which signals travel: copper, fiber or radio space.
2|Copper cable|Carries electrical signals through metal conductors.
2|Fiber-optic cable|Carries light signals through a glass or plastic core.
2|Wireless|Communication using electromagnetic waves without a physical cable between endpoints.
2|UTP|Unshielded Twisted Pair|Copper cable with twisted conductor pairs and no metallic shielding.
2|EMI|Electromagnetic Interference|Unwanted electromagnetic energy that can disturb signals.
2|Crosstalk|Interference from a signal in an adjacent wire or channel.
2|Bandwidth|A frequency range in hertz; in networking also commonly used to mean data-carrying capacity.
2|Bit rate|The number of transmitted bits per second.
2|Gbps|Gigabits per second|One billion bits per second, not bytes per second.
2|Noise|Unwanted variation that makes a signal harder to detect accurately.
2|Attenuation|Loss of signal strength as it travels through a medium.
2|Cat 5e|Copper Ethernet category commonly supporting 1 Gbps over a 100 m channel.
2|Cat 6|Copper Ethernet category supporting 1 Gbps at 100 m and 10 Gbps over shorter channels.
2|Cat 6a|Copper Ethernet category supporting 10 Gbps over a 100 m channel.
2|Cat 8|Shielded copper category for 25/40 Gbps channels up to 30 m; not UTP.
2|Total internal reflection|Light remains in the fiber core when it strikes the lower-index cladding above the critical angle.
2|Core|The central light-carrying portion of an optical fiber.
2|Cladding|The lower-refractive-index material around a fiber core that helps confine light.
2|Single-mode fiber|Fiber with an approximately 9 μm core, suitable for long-distance links with appropriate optics.
2|Multimode fiber|Fiber with a 50 or 62.5 μm core, carrying multiple light paths; usually used over shorter distances.
2|Amplitude|The magnitude or strength of a wave relative to its reference level.
2|Frequency|The number of wave cycles per second, measured in hertz.
2|Phase|A wave's position within its cycle relative to a reference.
2|Modulation|Changing a carrier's properties to represent information.
2|AM|Amplitude Modulation|Varying a carrier's amplitude; amplitude noise can corrupt it.
2|FM|Frequency Modulation|Varying a carrier's frequency; typically resists amplitude noise better than AM, often using more bandwidth.
2|PM|Phase Modulation|Varying a carrier's phase to represent information.
2|QAM|Quadrature Amplitude Modulation|Combines amplitude and phase changes. Higher orders carry more bits per symbol but need cleaner signals.
2|Multiplexing|Sharing one medium among multiple signals or users.
2|FDM|Frequency Division Multiplexing|Assigns different frequency bands to simultaneous users/signals.
2|TDM|Time Division Multiplexing|Assigns different time slots to users/signals.
3|Ethernet|A family of wired LAN technologies standardized by IEEE 802.3.
3|Frame|A data-link-layer unit carrying a header, payload and usually an error-checking trailer.
3|Packet|A network-layer unit, such as an IP packet, carried inside a link-layer frame.
3|Payload|The data carried by a protocol unit, excluding that protocol's overhead.
3|NIC|Network Interface Card|Hardware that connects a host to a network; also called a network interface controller.
3|MAC|Media Access Control|The link-layer addressing/access sublayer; an Ethernet MAC address is 48 bits.
3|OUI|Organizationally Unique Identifier|The first 24 bits in a traditional universally administered 48-bit MAC address.
3|Broadcast|A transmission sent to all devices in the local broadcast domain.
3|Unicast|A transmission addressed to one destination.
3|CSMA/CD|Carrier Sense Multiple Access with Collision Detection|Shared half-duplex Ethernet listens before transmitting and detects/responds to collisions.
3|Collision|Overlapping transmissions on a shared half-duplex medium that corrupt communication.
3|Backoff|A randomized wait before retrying after a collision.
3|Full duplex|Simultaneous sending and receiving; switched full-duplex Ethernet does not need CSMA/CD.
3|Half duplex|Communication in both directions, but not at the same time.
3|Preamble|A 7-byte Ethernet synchronization pattern preceding the SFD.
3|SFD|Start Frame Delimiter|The 1-byte marker after the preamble that signals the frame start.
3|Destination MAC|The receiver address in an Ethernet frame, not the sender address.
3|Source MAC|The sender address in an Ethernet frame.
3|EtherType|A field identifying the protocol carried inside an Ethernet II frame, such as IPv4.
3|Padding|Extra data added to satisfy a frame's minimum length.
3|FCS|Frame Check Sequence|An Ethernet error-detection field, normally 4 bytes.
3|CRC|Cyclic Redundancy Check|An error-detection calculation used to produce the Ethernet FCS.
3|MTU|Maximum Transmission Unit|The largest network-layer packet a link can carry without fragmentation; commonly 1500 bytes for Ethernet.
3|Bit|A binary digit, either 0 or 1.
3|Byte|A group of 8 bits.
3|Octet|Exactly 8 bits; each dotted IPv4 component is an octet.
3|Nibble|4 bits, equivalent to one hexadecimal digit.
3|Binary|Base-2 number notation, using digits 0 and 1.
3|Decimal|Base-10 number notation, using digits 0 through 9.
3|Hexadecimal|Base-16 notation, using 0–9 and A–F, where A=10 through F=15.
3|Hub|Repeats received signals to other ports on a shared collision domain.
3|Switch|Learns MAC-to-port mappings and forwards frames within a LAN.
3|STP|Spanning Tree Protocol|Prevents layer-2 loops by blocking redundant forwarding paths.
3|Topology|The arrangement of devices and links in a network.
3|Star topology|Endpoints connect to a central device, commonly a switch.
3|Bus topology|Devices share a common backbone cable.
3|Ring topology|Devices/links form a circular path.
3|Mesh topology|Devices have multiple interconnections; full mesh connects every pair.
3|VLAN|Virtual Local Area Network|A logical layer-2 broadcast domain formed on switches.
4|Router|A device that forwards packets between IP networks.
4|Routing|Selecting paths or next hops for packets to reach destination networks.
4|Routing table|Destination prefixes and associated forwarding information such as next hop and interface.
4|Next hop|The next router or destination to which a packet is sent.
4|IPv4|Internet Protocol version 4|Uses 32-bit addresses normally written as four decimal octets.
4|IPv6|Internet Protocol version 6|Uses 128-bit addresses written in hexadecimal groups separated by colons.
4|Network portion|The prefix bits identifying the IP network/subnet.
4|Host portion|The remaining address bits identifying a location/interface within the subnet.
4|CIDR|Classless Inter-Domain Routing|Uses variable-length prefixes written as /n instead of fixed address classes.
4|Prefix length|The number of network bits; /17 means 17 network bits in the address.
4|Subnet mask|For IPv4, 32 bits with 1s for network bits and 0s for host bits.
4|Network address|The address with all host bits set to 0 for a subnet.
4|Broadcast address|In a traditional IPv4 subnet, the address with all host bits set to 1.
4|Classful addressing|Historical fixed-size address classes; often wastes space compared with CIDR.
4|Hextet|A 16-bit IPv6 group written as up to four hexadecimal digits.
4|Zero compression|Replacing a run of all-zero IPv6 groups with ::; allowed only once per address.
4|ICMP|Internet Control Message Protocol|Carries IP diagnostic, status and error messages.
4|Ping|A utility using echo requests/replies to test reachability and round-trip time.
4|Traceroute|A utility discovering successive hops using increasing TTL or hop-limit values.
4|Pathping|A Windows utility combining route discovery with packet-loss and latency measurement.
4|TTL|Time To Live|An IPv4 hop counter reduced by routers to prevent indefinite packet looping.
4|Latency|The delay experienced by data; ping commonly measures round-trip latency.
4|Packet loss|Packets that fail to arrive at their destination.
4|RIR|Regional Internet Registry|An organization allocating/registering Internet number resources in a geographic region.
4|ARIN|American Registry for Internet Numbers|An RIR serving the United States, Canada and parts of the Caribbean.
4|RIPE NCC|Réseaux IP Européens Network Coordination Centre|An RIR serving Europe, the Middle East and parts of Central Asia.
4|APNIC|Asia Pacific Network Information Centre|The RIR serving the Asia-Pacific region.
4|LACNIC|Latin America and Caribbean Network Information Centre|An RIR serving Latin America and parts of the Caribbean.
4|AFRINIC|African Network Information Centre|The RIR serving Africa.
12|Requirements analysis|Identifying users, applications, sites, performance needs and constraints before designing a network.
12|Logical design|The network's logical layout, subnet structure, addressing, naming and management plan.
12|Physical design|The devices, media, technologies and placement used to implement a logical design.
12|Building network|A network connecting devices within one building.
12|Structured cabling|An organized system of building cabling, termination points, rooms and pathways.
12|Horizontal cabling|Cabling from a telecommunications room to work areas on a floor.
12|Vertical cabling|Backbone cabling connecting floors or telecommunications rooms.
12|Patch panel|A termination panel used to organize and connect cable runs.
12|Telecommunications room|A space housing cable terminations and related networking equipment.
12|Data center|A facility housing servers, storage and networking infrastructure.
12|Data center topology|The arrangement of server and network connections for reliable, high-capacity communication.
12|Spine-leaf|A common data-center topology connecting each leaf switch to each spine switch.
12|Campus network|A network connecting multiple nearby buildings.
12|Core layer|The high-speed, reliable backbone connecting distribution regions.
12|Distribution layer|Aggregates access networks and applies routing and network policies.
12|Access layer|Connects end-user devices to the network.
12|Backbone|The main interconnection system carrying traffic between network regions.
12|Enterprise network|An organization's interconnected networks, often spanning distant locations.
12|WAN|Wide Area Network|Connects networks over a broad geographic area.
12|ISP|Internet Service Provider|Provides Internet connectivity and may provide WAN services.
12|Firewall|A system enforcing traffic rules between networks or hosts.
12|Authentication|Verifying an identity before granting access.
12|Network maintenance|Inspection, testing, monitoring, servicing, backups and hardware/software updates.
12|Downtime|A period when a service is unavailable, with costs from interrupted work.
12|SNMP|Simple Network Management Protocol|Allows a manager to read/manage device information and receive notifications.
12|MIB|Management Information Base|A structured collection of managed objects exposed to network management systems.
12|OID|Object Identifier|A hierarchical identifier for a managed object in an MIB.
12|Polling|A manager periodically requesting status or values from managed devices.
12|SNMP agent|Software on a managed device that exposes management information.
12|SNMP trap|An unsolicited event notification sent from an agent to a manager.
12|Standard|A consensus specification intended to support consistent, interoperable implementations.
12|Working group|A group developing and reviewing a technical specification or standard.`;
const VOCAB=vocabRows.split('\n').map((line,i)=>{let [ch,term,a,b]=line.split('|');return {id:'v'+i,ch:+ch,term,exp:b?a:null,a:b||a,q:b?`What does ${term} stand for?`:`Define ${term}.`}});
