import axios from "axios";

const API_URL = "https://expense-tracker-o1dq.onrender.com";

export const getExpenses = async () => {
  const res = await axios.get(`${API_URL}/expenses/`);
  return res.data;
};

export const addExpense = async (expense) => {
  const res = await axios.post(`${API_URL}/expenses/`, expense);
  return res.data;
};