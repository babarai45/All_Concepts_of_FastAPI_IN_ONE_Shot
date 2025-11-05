<div align="center">

<h1> What is Request </h1>

</div>

<hr>

![img](assets/img.png)

<hr>

![waht_is_request](assets/requet-iclude.png)






<hr>

In an **API** (Application Programming Interface), a **request** is how a client (like your app, website, or program) asks a server to perform an action or provide some data.

Let’s break it down simply 👇

---

### 🧩 **What is an API request?**

An **API request** is a message sent from a **client** to a **server**, asking it to do something — such as:

* Retrieve data (like user info or weather)
* Create new data (like adding a new post)
* Update existing data
* Delete data

---

### 🧠 **What does a request include?**

An API request usually has these parts:

| Part                   | Description                                 | Example                         |
| ---------------------- | ------------------------------------------- | ------------------------------- |
| **Endpoint (URL)**     | The address of the API you’re calling       | `https://api.example.com/users` |
| **Method (HTTP verb)** | The action you want to perform              | `GET`, `POST`, `PUT`, `DELETE`  |
| **Headers**            | Metadata (like authentication, format info) | `Authorization: Bearer <token>` |
| **Body (optional)**    | Data you send to the server (for POST/PUT)  | `{ "name": "Alice" }`           |

---

### ⚙️ **Example**

If you wanted to get a list of users from an API:

```http
GET https://api.example.com/users
```

If you wanted to add a new user:

```http
POST https://api.example.com/users
Content-Type: application/json

{
  "name": "Alice",
  "email": "alice@example.com"
}
```

---

### 🗣️ **In short**

> A “request” in an API is how your program *asks* a server for something — it’s like saying, “Hey server, please give me this data,” or “Hey, please save this new record.”

---

<div align="center">
<h3> Happy Learning by Muhammad Babar 🥰</h3>
</div>
