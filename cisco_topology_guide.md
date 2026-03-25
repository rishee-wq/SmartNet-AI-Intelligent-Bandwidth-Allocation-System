# SmartNet AI — Basic Cisco Topology Guide

## 1. Required Devices
- 1 x Router (2911)
- 1 x Switch (2960)
- 3 x PCs (PC1, PC2, PC3)

## 2. Physical Connections
- R1 (G0/0) <---> S1 (G0/1)
- S1 (Fa0/1) <---> PC1 (Critical)
- S1 (Fa0/2) <---> PC2 (High)
- S1 (Fa0/3) <---> PC3 (Low)

## 3. Switch Configuration (S1)
```cisco
vlan 10
 name CRITICAL
vlan 20
 name HIGH
vlan 30
 name LOW
interface range f0/1
 switchport access vlan 10
interface range f0/2
 switchport access vlan 20
interface range f0/3
 switchport access vlan 30
interface g0/1
 switchport mode trunk
```

## 4. Router Configuration (R1 - Router-on-a-Stick)
```cisco
interface g0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 service-policy output SMARTNET_AI_POLICY
interface g0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 service-policy output SMARTNET_AI_POLICY
interface g0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 service-policy output SMARTNET_AI_POLICY
```

---

## 5. Router QoS Configuration (R1)

```cisco
enable
configure terminal

! Interface to core switch
interface GigabitEthernet0/0
 ip address 10.0.0.1 255.255.255.0
 no shutdown
 exit

! Routes to VLANs
ip route 192.168.10.0 255.255.255.0 10.0.0.2
ip route 192.168.20.0 255.255.255.0 10.0.0.2
ip route 192.168.30.0 255.255.255.0 10.0.0.2

! ===== SmartNet AI QoS Policy =====

! Define ACL for VoIP
access-list 101 permit udp any any range 16384 32767

! Class maps
class-map match-any CRITICAL_TRAFFIC
 match access-group 101
 match protocol rtp
 match dscp ef

class-map match-any HIGH_TRAFFIC
 match protocol http
 match protocol https
 match dscp af31

class-map match-any MEDIUM_TRAFFIC
 match protocol dns
 match protocol smtp
 match dscp af21

class-map match-any LOW_TRAFFIC
 match protocol ftp
 match dscp default

! Policy map — SmartNet AI bandwidth allocation
policy-map SMARTNET_AI_POLICY
 class CRITICAL_TRAFFIC
  priority percent 40
  set dscp ef
 class HIGH_TRAFFIC
  bandwidth percent 30
  set dscp af31
 class MEDIUM_TRAFFIC
  bandwidth percent 20
  set dscp af21
 class LOW_TRAFFIC
  bandwidth percent 10
  set dscp default
 class class-default
  fair-queue

! Apply to interface
interface GigabitEthernet0/0
 service-policy output SMARTNET_AI_POLICY

end
write memory
```

---

## 6. End Device IP Configuration

| Device   | IP Address       | Subnet Mask      | Default Gateway  |
|----------|------------------|-------------------|------------------|
| PC1      | 192.168.10.10    | 255.255.255.0     | 192.168.10.1     |
| IP Phone | 192.168.10.11    | 255.255.255.0     | 192.168.10.1     |
| PC3      | 192.168.20.10    | 255.255.255.0     | 192.168.20.1     |
| PC4      | 192.168.20.11    | 255.255.255.0     | 192.168.20.1     |
| PC5      | 192.168.30.10    | 255.255.255.0     | 192.168.30.1     |
| Server1  | 192.168.30.100   | 255.255.255.0     | 192.168.30.1     |

---

## 7. Verification Commands

```cisco
! Verify VLANs
show vlan brief

! Verify inter-VLAN routing
show ip route

! Verify QoS policy
show policy-map interface GigabitEthernet0/0

! Verify connectivity
ping 192.168.10.10
ping 192.168.20.10
ping 192.168.30.100

! Show interface statistics
show interfaces GigabitEthernet0/0
```

---

## 8. Testing Traffic Flow

1. **Ping test**: From PC1, ping PC3 and PC5 to verify inter-VLAN routing.
2. **Web traffic**: Set up HTTP server on Server1, access from PC3/PC4.
3. **VoIP simulation**: Use IP Phone to call (if call manager is configured).
4. **Bandwidth test**: Use simulation mode to observe QoS markings on packets.

---

## 9. Connecting ML Model to Topology

The Decision Tree model's classification rules translate to Cisco QoS as:

| ML Class → | Cisco Class Map      | DSCP Marking | Queue Type    | BW % |
|------------|---------------------|--------------|---------------|------|
| Critical   | CRITICAL_TRAFFIC    | EF           | Priority      | 40%  |
| High       | HIGH_TRAFFIC        | AF31         | CBWFQ         | 30%  |
| Medium     | MEDIUM_TRAFFIC      | AF21         | CBWFQ         | 20%  |
| Low        | LOW_TRAFFIC         | Default      | CBWFQ         | 10%  |

The extracted Decision Tree rules can be manually converted to additional ACLs
for more granular traffic matching in the Packet Tracer environment.
