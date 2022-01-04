import "./App.scss";

import React from "react";
import { Routes, Route } from "react-router-dom";
import Header from "../header";
import { HomePage, LoginPage, RegisterPage } from "../../pages";
import { Container } from "@mui/material";

const App = (props) => {
    return (
        <div className="app">
            <Header {...props} />
            <Container sx={{ paddingTop: "60px" }}>
                <Routes>
                    <Route exec path="/" element={<HomePage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<RegisterPage />} />
                    <Route
                        path="*"
                        render={() => <h1>This page not found!</h1>}
                    />
                </Routes>
            </Container>
        </div>
    );
};

export default App;
