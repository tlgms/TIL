<!-- notion-page-id: 3a02cdd741ac80c2b920e8a050374d3b -->

# Port 번호 / IP 주소 / Mac 주소

## 1. 식별자

```mermaid
flowchart LR
    subgraph UM["user mode"]
        L7b["L7"]
    end
    subgraph KM["kernel mode"]
        TS["전송 (Transport)"]
        NT["Net"]
    end
    subgraph HW["H/W (인터페이스 번호?)"]
        L1b["… L1"]
    end

    TS -->|"port 번호"| SVC["Service? / Process?"]
    NT -->|"IP 주소 (v4, v6)"| HOST(["host"])
    L1b -->|"Mac 주소"| NICB["NIC (LAN 카드)<br/>유선/무선"]
    NICB --> COMP["인터넷에 연결된 컴퓨터"]
```

각 식별자가 가리키는 대상:

### 포스트잇 메모

- 노트북 ← NIC 2개 (유선/무선) → **Mac 주소 2개**

- 컴퓨터 ← IP 주소 몇 개? → **N개**

- **Mac 주소 하나에 여러 IP를 매핑(바인딩)함**
