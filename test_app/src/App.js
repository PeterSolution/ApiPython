import React, { useEffect, useState } from "react";

const UsersTable = () => {
  const [users, setUsers] = useState([]);
  const [editingUserId, setEditingUserId] = useState(null);
  const [formData, setFormData] = useState({ name: "", email: "", password: "" });
  const [newUserData, setNewUserData] = useState({ name: "", email: "", password: "" });
  const [searchId, setSearchId] = useState("");
  const [searchedUser, setSearchedUser] = useState(null);

  const fetchUsers = async () => {
    const res = await fetch("http://localhost:5000/users");
    const data = await res.json();
    setUsers(data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  // Dodawanie nowego użytkownika
  const handleAddUser = async () => {
    const res = await fetch("http://localhost:5000/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newUserData),
    });
    const data = await res.json();
    setUsers([...users, data]);
    setNewUserData({ name: "", email: "", password: "" });
  };

  // Edycja użytkownika
  const handleEdit = (user) => {
    setEditingUserId(user.id);
    setFormData({ name: user.name, email: user.email, password: "" });
  };

  const handleCancel = () => {
    setEditingUserId(null);
    setFormData({ name: "", email: "", password: "" });
  };

  const handleSave = async (id) => {
    await fetch(`http://localhost:5000/users/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });
    setEditingUserId(null);
    fetchUsers();
  };

  const handleDelete = async (id) => {
    await fetch(`http://localhost:5000/users/${id}`, { method: "DELETE" });
    setUsers(users.filter(user => user.id !== id));
  };

  // Wyszukiwanie użytkownika po ID
  const handleSearch = async () => {
    if (!searchId) return setSearchedUser(null);
    const res = await fetch(`http://localhost:5000/users`);
    const data = await res.json();
    const user = data.find(u => u.id === parseInt(searchId));
    setSearchedUser(user || null);
  };

  return (
    <div>
      <h2>Dodaj nowego użytkownika</h2>
      <input
        type="text"
        placeholder="Name"
        value={newUserData.name}
        onChange={(e) => setNewUserData({ ...newUserData, name: e.target.value })}
      />
      <input
        type="email"
        placeholder="Email"
        value={newUserData.email}
        onChange={(e) => setNewUserData({ ...newUserData, email: e.target.value })}
      />
      <input
        type="password"
        placeholder="Password"
        value={newUserData.password}
        onChange={(e) => setNewUserData({ ...newUserData, password: e.target.value })}
      />
      <button onClick={handleAddUser}>Dodaj</button>

      <h2>Wyszukaj użytkownika po ID</h2>
      <input
        type="number"
        placeholder="User ID"
        value={searchId}
        onChange={(e) => setSearchId(e.target.value)}
      />
      <button onClick={handleSearch}>Szukaj</button>
      {searchedUser && (
        <div>
          <h3>Znaleziony użytkownik:</h3>
          <p>ID: {searchedUser.id}</p>
          <p>Name: {searchedUser.name}</p>
          <p>Email: {searchedUser.email}</p>
        </div>
      )}

      <h2>Lista użytkowników</h2>
      <table border="1" cellPadding="5" cellSpacing="0">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Password</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>
                {editingUserId === user.id ? (
                  <input
                    type="text"
                    value={formData.name}
                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  />
                ) : (
                  user.name
                )}
              </td>
              <td>
                {editingUserId === user.id ? (
                  <input
                    type="email"
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  />
                ) : (
                  user.email
                )}
              </td>
              <td>
                {editingUserId === user.id ? (
                  <input
                    type="password"
                    placeholder="New password"
                    value={formData.password}
                    onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                  />
                ) : (
                  "********"
                )}
              </td>
              <td>
                {editingUserId === user.id ? (
                  <>
                    <button onClick={() => handleSave(user.id)}>Save</button>
                    <button onClick={handleCancel}>Cancel</button>
                  </>
                ) : (
                  <>
                    <button onClick={() => handleEdit(user)}>Edit</button>
                    <button onClick={() => handleDelete(user.id)}>Delete</button>
                  </>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UsersTable;
