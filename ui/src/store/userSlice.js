import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const userSlice = createSlice({
    name: "user",
    initialState: {
        data: null,
        status: null,
        error: null,
    },
    reducers: {},
});

export default userSlice.reducer;
