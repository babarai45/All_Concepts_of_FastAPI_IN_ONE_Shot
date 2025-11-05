<div align="center">

<h1> Types of API </h1>

</div>

<hr>
<hr>

![tyeps-api.png](assets/tyeps-api.png)



<hr>



## 🔓 1. By Availability / Access

| Type                      | 💬 Description                          | ✅ Pros                                          | ⚠️ Cons                                      | 💡 Examples                       |
| :------------------------ | :-------------------------------------- | :---------------------------------------------- | :------------------------------------------- | :-------------------------------- |
| **🌍 Public (Open)**      | Open to everyone for external use.      | 💡 Innovation <br> 🌱 Ecosystem <br> 💰 Revenue | 🔒 Security risks <br> 🧾 Support needed     | Google Maps, Stripe, Spotify      |
| **🤝 Partner**            | Shared with specific business partners. | 🔐 Secure <br> 🤝 Aligned goals                 | 🚫 Limited reach <br> 🧩 Partner mgmt needed | Airline–Hotel integrations        |
| **🏢 Private (Internal)** | Used only inside an organization.       | ⚙️ Efficiency <br> 🔐 Full control              | 🏠 Internal scope only                       | HR ↔ Payroll API                  |
| **🧩 Composite**          | Combines multiple APIs in one call.     | ⚡ Fast <br> ✨ Simplified                        | 🔧 Complex backend                           | Checkout API (payment + shipping) |

---

## ⚙️ 2. By Architecture / Protocol

| Type             | 💬 Description                            | ✅ Pros                              | ⚠️ Cons                                    | 💡 Use Case                   |
| :--------------- | :---------------------------------------- | :---------------------------------- | :----------------------------------------- | :---------------------------- |
| **🌐 REST**      | Uses HTTP + JSON, stateless.              | 🧠 Simple <br> 📈 Scalable          | 📦 Over/under-fetching                     | Web & mobile APIs             |
| **📜 SOAP**      | XML-based protocol with strict standards. | 🧱 Reliable <br> 🔒 Secure          | 🐢 Heavy & verbose                         | Banking, enterprise systems   |
| **🔍 GraphQL**   | Query language for APIs.                  | 🎯 Precise data <br> 💬 Single call | ⚙️ Complex backend                         | Complex UIs, mobile apps      |
| **🚀 gRPC**      | High-performance via HTTP/2 + Protobuf.   | ⚡ Super fast <br> 🔄 Streaming      | 🧩 Harder to debug                         | Microservices, real-time apps |
| **💬 WebSocket** | Full-duplex real-time connection.         | ⚡ Live updates <br> 🔁 Persistent   | 🌪️ Harder to scale                        | Chat, games, live feeds       |
| **📢 Webhook**   | Event-triggered HTTP callbacks.           | ⏱️ Instant <br> 💡 Efficient        | 🧱 Requires uptime <br> 🔒 Security checks | Stripe, GitHub, forms         |

---

## 🎯 3. By Use Case

* **📊 Data APIs:** Access datasets (weather, finance, gov).
* **⚙️ Service APIs:** Provide functions (payments, email, translation).
* **🔌 Hardware APIs:** Interact with device sensors (camera, GPS).
* **🖥️ OS APIs:** Access system-level features (Windows, POSIX).
* **📚 Library APIs:** Use code libraries (Java, Python `requests`).

---

## 🧭 Summary

| Role                          | Focus                                  | Best Picks                                            |
| :---------------------------- | :------------------------------------- | :---------------------------------------------------- |
| 💼 **Business/Product**       | Access type (Public, Partner, Private) | 🌍 Public APIs grow ecosystems                        |
| 👨‍💻 **Developer/Architect** | Architecture (REST, GraphQL, gRPC)     | 🧠 REST = simple, ⚡ gRPC = fast, 🎯 GraphQL = precise |

---

✨ **REST** rules for simplicity, **GraphQL** for smart data fetching, and **gRPC** for lightning-fast microservices. 🚀
