import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export const getExpenses = async () => {
  const res = await axios.get(`${API_URL}/expenses`);
  return res.data;
};

export const addExpense = async (expense) => {
  const res = await axios.post(`${API_URL}/expenses`, expense);
  return res.data;
};