const form = document.getElementById("transaction-form");
const list = document.getElementById("transaction-list");

let transactions = JSON.parse(localStorage.getItem("transactions")) || [];

function renderTransactions() {
  list.innerHTML = "";
  transactions.forEach((t, i) => {
    const li = document.createElement("li");
    li.textContent = `${t.description} - $${t.amount} (${t.type}, ${t.category})`;
    list.appendChild(li);
  });
}

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const description = document.getElementById("description").value;
  const amount = parseFloat(document.getElementById("amount").value);
  const type = document.getElementById("type").value;
  const category = document.getElementById("category").value || "Uncategorized";

  transactions.push({ description, amount, type, category });
  localStorage.setItem("transactions", JSON.stringify(transactions));
  renderTransactions();
  form.reset();
});

renderTransactions();
