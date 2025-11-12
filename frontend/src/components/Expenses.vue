<template>
  <div class="expenses">
    <h1>💰 Expense Tracker</h1>

    <!-- Add new expense form -->
    <form @submit.prevent="addNewExpense" class="expense-form">
      <input v-model="newExpense.title" placeholder="Title" />
      <input v-model.number="newExpense.amount" placeholder="Amount" type="number" />
      <input v-model="newExpense.category" placeholder="Category" />
      <button type="submit">Add Expense</button>
    </form>

    <hr />

    <!-- Display expenses -->
    <div v-if="expenses.length === 0">No expenses found.</div>
    <ul v-else>
      <li v-for="(expense, index) in expenses" :key="index">
        <strong>{{ expense.title }}</strong> — ₹{{ expense.amount }} ({{ expense.category }})
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getExpenses, addExpense } from "../api";

const expenses = ref([]);
const newExpense = ref({ title: "", amount: "", category: "" });

// Fetch expenses on component load
const loadExpenses = async () => {
  expenses.value = await getExpenses();
};

// Add a new expense
const addNewExpense = async () => {
  if (!newExpense.value.title || !newExpense.value.amount) return;
  await addExpense(newExpense.value);
  newExpense.value = { title: "", amount: "", category: "" };
  await loadExpenses();
};

// Run on page load
onMounted(loadExpenses);
</script>

<style scoped>
.expenses {
  max-width: 500px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.expense-form input {
  margin: 5px;
  padding: 6px;
}

button {
  background: #007bff;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background: #0056b3;
}
</style>
