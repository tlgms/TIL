<!-- notion-page-id: 3a02cdd741ac8003846dcca0704e7713 -->

# Network

> **Internet ≒ ① Ⓡ(Router) + ② DNS**

## 계층별 식별자와 구현

```mermaid
flowchart LR
    subgraph U["user mode"]
        L7["L7 ← http"]
    end
    subgraph K["kernel mode"]
        PORT["Port · L4"] --> TCP["TCP"]
        IP3["IP · L3"] --> IPP["IP"]
    end
    subgraph HW["H/W"]
        MAC["MAC · L2"] --> ETH["Ethernet (유선)<br/>802.11~ (무선)"]
    end
    TCP -. "서로 계층이 다르지만<br/>TCP/IP로 함께 불림" .- IPP
```

### 메모

- Mac 주소는 하드웨어 주소지만, OSI 7 Layer에서 **L2에 존재**한다.

- Switching 하는 위치에 따라 **Mac은 L2 switch, IP는 L3, Port는 L4**이다.
  - 
    - http는 **L7 스위치**

- switch는 OSI 7 Layer 레벨이 오를수록 비싸진다. ⇒ **위로 갈수록 연산이 복잡해진다.**

- TCP/IP는 서로 계층이 다르지만, 서로 **실과 바늘 같은 관계**라서 꼭 함께 불린다.

---

## 포스트잇: OSI 7 Layer ↔ TCP/IP Protocol

```mermaid
flowchart LR
    subgraph OSI["OSI 7 Layer"]
        direction TB
        A1["application (응용)"]
        A2["presentation (표현)"]
        A3["session (세션)"]
        A4["transport (전송)"]
        A5["network (네트워크)"]
        A6["data link (데이터 링크)"]
        A7["physical (물리)"]
        A1 --- A2 --- A3 --- A4 --- A5 --- A6 --- A7
    end

    subgraph TCPIP["TCP/IP Protocol"]
        direction TB
        B1["application (응용)"]
        B2["전송 계층"]
        B3["인터넷 계층"]
        B4["네트워크 접근 계층"]
        B1 --- B2 --- B3 --- B4
    end

    A1 -.-> B1
    A2 -.-> B1
    A3 -.-> B1
    A4 -.-> B2
    A5 -.-> B3
    A6 -.-> B4
    A7 -.-> B4
```

### 계층별 대표 프로토콜
