import './App.scss';

import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import TodoList from './TodoList';
import InputField from './InputField';
import { addNewTodo, fetchTodos } from '../store/todoSlice';

const App = () => {
    const dispatch = useDispatch();
    const { status, error } = useSelector((state) => state.todos);
    const [text, setText] = useState('');

    const addTask = () => {
        dispatch(addNewTodo(text));
        setText('');
    };

    useEffect(() => {
        dispatch(fetchTodos());
    }, [dispatch]);

    return (
        <>
            <div className="app">
                <InputField
                    text={text}
                    handleInput={setText}
                    handleSubmit={addTask}
                />
                {status === 'loading' && <h2>Loading</h2>}
                {error && <h2>An error occured: {error}</h2>}

                <TodoList />
            </div>
        </>
    );
};

export default App;
