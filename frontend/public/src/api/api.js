import axios from "axios";

const API_BASE_URL = "http://localhost:5000/api"; // Change when deploying

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const loginUser = async (email, password) => {
  return api.post("/login", { email, password });
};

export const registerUser = async (username, email, password) => {
  return api.post("/register", { username, email, password });
};
