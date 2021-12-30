import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
    const [users, setUsers] = useState([]);
    
    axios
        .get("http://localhost:8001/api/users/")
        .then((res) => setUsers([res]))
        .catch((err) => console.log(err));

    console.log(users);

    return (
        <>
            <h1>Hello</h1>
        </>
    );
};

export default App;
