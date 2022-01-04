const setError = (state, action) => {
    state.status = "rejected";
    state.error = action.payload;
};

const setLoad = (state) => {
    state.status = "loading";
    state.error = null;
};

export { setError, setLoad };
