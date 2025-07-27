// Data storage
  let inventory = JSON.parse(localStorage.getItem('chathurInventory')) || [];
  let bills = JSON.parse(localStorage.getItem('chathurBills')) || [];
  let billCounter = bills.length > 0 ? Math.max(...bills.map(b => b.id)) + 1 : 1001;
  let currentPaymentBill = null; 
 // DOM elements
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('.section');
  const addProductBtn = document.getElementById('add-product-btn');
  const productForm = document.getElementById('product-form');
  const cancelProductBtn = document.getElementById('cancel-product');
  const saveProductBtn = document.getElementById('save-product');
  const inventoryBody = document.getElementById('inventory-body');
  const addProductBillBtn = document.getElementById('add-product-bill');
  const billItemsBody = document.getElementById('bill-items-body');
  const generateBillBtn = document.getElementById('generate-bill');
  const amountPaidInput = document.getElementById('amount-paid');
  const paymentsTableBody = document.querySelector('#payments-table tbody');
  const billsTableBody = document.querySelector('#bills-table tbody');
  const recentTransactionsBody = document.querySelector('#recent-transactions tbody');
  const viewAllBillsBtn = document.getElementById('view-all-bills');
  const refreshBillsBtn = document.getElementById('refresh-bills');
  const paymentModal = document.getElementById('payment-modal');
  const closeModalBtn = document.querySelector('.close-modal');
  const cancelPaymentBtn = document.getElementById('cancel-payment');
  const savePaymentBtn = document.getElementById('save-payment');
 
 // Initialize
 document.addEventListener('DOMContentLoaded', function() {
     document.getElementById('bill-date').valueAsDate = new Date();
     renderInventory();
     renderPayments();
     renderBills();
     updateDashboard();
 });
 
 // Navigation functionality
 navLinks.forEach(link => {
     link.addEventListener('click', function(e) {
         e.preventDefault();
         
         // Update active nav item
         navLinks.forEach(item => item.classList.remove('active'));
         this.classList.add('active');
         
         // Show active section
         const targetId = this.getAttribute('data-target');
         sections.forEach(section => section.classList.remove('active'));
         document.getElementById(targetId).classList.add('active');
     });
 });
 
 // Toggle product form
 if (addProductBtn && productForm && cancelProductBtn) {
     addProductBtn.addEventListener('click', () => {
         productForm.style.display = 'grid';
         addProductBtn.style.display = 'none';
     });
     
     cancelProductBtn.addEventListener('click', () => {
         productForm.style.display = 'none';
         addProductBtn.style.display = 'block';
         resetProductForm();
     });
 }
 
 // Save product to inventory
 saveProductBtn.addEventListener('click', saveProduct);
 
 // Add product to bill
 addProductBillBtn.addEventListener('click', addProductToBill);
 
 // Generate bill
 generateBillBtn.addEventListener('click', generateBill);
 
 // View all bills
 viewAllBillsBtn.addEventListener('click', () => {
     navLinks.forEach(item => item.classList.remove('active'));
     document.querySelector('.nav-link[data-target="bills"]').classList.add('active');
     sections.forEach(section => section.classList.remove('active'));
     document.getElementById('bills').classList.add('active');
 });
 
 // Refresh bills
 refreshBillsBtn.addEventListener('click', renderBills);
 
 // Payment modal
 closeModalBtn.addEventListener('click', closePaymentModal);
 cancelPaymentBtn.addEventListener('click', closePaymentModal);
 savePaymentBtn.addEventListener('click', savePayment);
 
 // Event listeners for real-time updates
 amountPaidInput.addEventListener('input', updateBillSummary);
 
 // Functions
 function resetProductForm() {
     document.getElementById('product-name').value = '';
     document.getElementById('product-quantity').value = '';
     document.getElementById('product-unit').value = 'KG';
     document.getElementById('buying-rate').value = '';
     document.getElementById('selling-rate').value = '';
     document.getElementById('product-description').value = '';
 }
 
 function saveProduct() {
     const productName = document.getElementById('product-name').value.trim();
     const quantity = parseFloat(document.getElementById('product-quantity').value);
     const unit = document.getElementById('product-unit').value;
     const buyingRate = parseFloat(document.getElementById('buying-rate').value);
     const sellingRate = document.getElementById('selling-rate').value ? parseFloat(document.getElementById('selling-rate').value) : buyingRate * 1.2;
     const description = document.getElementById('product-description').value.trim();
     
     if (!productName || isNaN(quantity) || isNaN(buyingRate) || quantity <= 0 || buyingRate <= 0) {
         showToast('Please fill all required fields with valid values', 'error');
         return;
     }
     
     // Create product object
     const product = {
         id: Date.now(),
         name: productName,
         quantity: quantity,
         unit: unit,
         buyingRate: buyingRate,
         sellingRate: sellingRate,
         description: description,
         createdAt: new Date().toISOString()
     };
     
     // Add to inventory
     inventory.push(product);
     localStorage.setItem('chathurInventory', JSON.stringify(inventory));
     
     // Show success message
     showToast('Product added to inventory successfully!');
     
     // Reset form and update UI
     resetProductForm();
     productForm.style.display = 'none';
     addProductBtn.style.display = 'block';
     renderInventory();
     updateDashboard();
 }
 
 function renderInventory() {
     inventoryBody.innerHTML = '';
     
     if (inventory.length === 0) {
         inventoryBody.innerHTML = `
             <tr>
                 <td colspan="7" class="empty-state">
                     <i class="fas fa-box-open"></i>
                     <p>No products in inventory. Add your first stock item!</p>
                 </td>
             </tr>
         `;
         return;
     }
     
     inventory.forEach(product => {
         const row = document.createElement('tr');
         row.innerHTML = `
             <td>CT-${product.id.toString().slice(-4)}</td>
             <td>${product.name}</td>
             <td>${product.description || '-'}</td>
             <td>${product.quantity} ${product.unit}</td>
             <td>₹${product.buyingRate.toFixed(2)}</td>
             <td>₹${product.sellingRate.toFixed(2)}</td>
             <td>
                 <button class="action-btn delete-btn" data-id="${product.id}"><i class="fas fa-trash"></i></button>
             </td>
         `;
         inventoryBody.appendChild(row);
     });
     
     // Add delete event listeners
     document.querySelectorAll('.delete-btn').forEach(btn => {
         btn.addEventListener('click', function() {
             const productId = parseInt(this.getAttribute('data-id'));
             deleteProduct(productId);
         });
     });
 }
 
 function deleteProduct(productId) {
     if (confirm('Are you sure you want to delete this product from inventory?')) {
         inventory = inventory.filter(product => product.id !== productId);
         localStorage.setItem('chathurInventory', JSON.stringify(inventory));
         renderInventory();
         updateDashboard();
         showToast('Product deleted successfully!');
     }
 }
 
 function addProductToBill() {
     if (inventory.length === 0) {
         showToast('No products available. Please add products to inventory first.', 'error');
         return;
     }
     
     const row = document.createElement('tr');
     row.innerHTML = `
         <td>
             <select class="bill-product-select">
                 <option value="">Select Product</option>
                 ${inventory.map(product => 
                     `<option value="${product.id}" 
                         data-selling-rate="${product.sellingRate}"
                         data-quantity="${product.quantity}"
                         data-unit="${product.unit}"
                         data-description="${product.description || ''}">
                         ${product.name}
                     </option>`
                 ).join('')}
             </select>
         </td>
         <td class="bill-description">-</td>
         <td class="bill-available">-</td>
         <td><input type="number" class="bill-quantity" value="1" min="0.01" step="0.01"></td>
         <td class="bill-unit">-</td>
         <td><input type="number" class="bill-rate" min="0.01" step="0.01"></td>
         <td class="bill-total">₹0.00</td>
         <td><button class="action-btn delete-btn"><i class="fas fa-trash"></i></button></td>
     `;
     billItemsBody.appendChild(row);
     
     // Add event listeners
     const productSelect = row.querySelector('.bill-product-select');
     const quantityInput = row.querySelector('.bill-quantity');
     const rateInput = row.querySelector('.bill-rate');
     const deleteBtn = row.querySelector('.delete-btn');
     
     productSelect.addEventListener('change', function() {
         const selectedOption = this.options[this.selectedIndex];
         const unit = selectedOption.getAttribute('data-unit') || '-';
         const description = selectedOption.getAttribute('data-description') || '-';
         const available = selectedOption.getAttribute('data-quantity') || '-';
         const sellingRate = parseFloat(selectedOption.getAttribute('data-selling-rate')) || 0;
         
         row.querySelector('.bill-unit').textContent = unit;
         row.querySelector('.bill-description').textContent = description;
         row.querySelector('.bill-available').textContent = `${available} ${unit}`;
         rateInput.value = sellingRate.toFixed(2);
         calculateBillTotal(row);
         updateBillSummary();
     });
     
     quantityInput.addEventListener('input', () => calculateBillTotal(row));
     rateInput.addEventListener('input', () => calculateBillTotal(row));
     deleteBtn.addEventListener('click', function() {
         row.remove();
         updateBillSummary();
     });
 }
 
 function calculateBillTotal(row) {
     const quantity = parseFloat(row.querySelector('.bill-quantity').value) || 0;
     const rate = parseFloat(row.querySelector('.bill-rate').value) || 0;
     const total = quantity * rate;
     row.querySelector('.bill-total').textContent = `₹${total.toFixed(2)}`;
     updateBillSummary();
 }
 
 function updateBillSummary() {
     let subtotal = 0;
     document.querySelectorAll('#bill-items-body tr').forEach(row => {
         const totalText = row.querySelector('.bill-total').textContent;
         const totalValue = parseFloat(totalText.replace('₹', '')) || 0;
         subtotal += totalValue;
     });
     
     const total = subtotal;
     const amountPaid = parseFloat(amountPaidInput.value) || 0;
     const pending = total - amountPaid;
     
     document.getElementById('subtotal').textContent = `₹${subtotal.toFixed(2)}`;
     document.getElementById('total-amount').textContent = `₹${total.toFixed(2)}`;
     document.getElementById('pending-amount').textContent = `₹${pending.toFixed(2)}`;
 }
 
 function generateBill() {
     const customerName = document.getElementById('customer-name').value.trim();
     const billDate = document.getElementById('bill-date').value;
     const amountPaid = parseFloat(amountPaidInput.value) || 0;
     const totalAmount = parseFloat(document.getElementById('total-amount').textContent.replace('₹', ''));
     
     if (!customerName) {
         showToast('Please enter company name', 'error');
         return;
     }
     
     const billItems = [];
     let isValid = true;
     
     document.querySelectorAll('#bill-items-body tr').forEach(row => {
         const productSelect = row.querySelector('.bill-product-select');
         const productId = parseInt(productSelect.value);
         const product = inventory.find(p => p.id === productId);
         
         if (!product) {
             isValid = false;
             return;
         }
         
         const quantity = parseFloat(row.querySelector('.bill-quantity').value);
         const rate = parseFloat(row.querySelector('.bill-rate').value);
         const total = quantity * rate;
         
         if (quantity > product.quantity) {
             showToast(`Not enough stock for ${product.name}. Available: ${product.quantity} ${product.unit}`, 'error');
             isValid = false;
             return;
         }
         
         billItems.push({
             productId: product.id,
             name: product.name,
             quantity: quantity,
             unit: product.unit,
             rate: rate,
             total: total
         });
     });
     
     if (billItems.length === 0) {
         showToast('Please add at least one product to the bill', 'error');
         return;
     }
     
     if (!isValid) return;
     
     // Create bill object
     const bill = {
         id: billCounter++,
         customer: customerName,
         date: billDate,
         items: billItems,
         total: totalAmount,
         paid: amountPaid,
         pending: totalAmount - amountPaid,
         status: amountPaid === 0 ? 'Pending' : (amountPaid < totalAmount ? 'Partial' : 'Paid')
     };
     
     // Add to bills
     bills.push(bill);
     localStorage.setItem('chathurBills', JSON.stringify(bills));
     
     // Update inventory
     billItems.forEach(item => {
         const product = inventory.find(p => p.id === item.productId);
         if (product) {
             product.quantity -= item.quantity;
         }
     });
     localStorage.setItem('chathurInventory', JSON.stringify(inventory));
     
     // Show success message
     showToast('Bill generated successfully!');
     
     // Reset form
     billItemsBody.innerHTML = '';
     document.getElementById('customer-name').value = '';
     amountPaidInput.value = '0';
     updateBillSummary();
     
     // Update UI
     renderInventory();
     renderPayments();
     renderBills();
     updateDashboard();
 }
 
 function renderPayments() {
     paymentsTableBody.innerHTML = '';
     
     if (bills.length === 0) {
         paymentsTableBody.innerHTML = `
             <tr>
                 <td colspan="9" class="empty-state">
                     <i class="fas fa-file-invoice"></i>
                     <p>No payment records found. Generate your first bill!</p>
                 </td>
             </tr>
         `;
         return;
     }
     
     bills.forEach(bill => {
         const dueDate = new Date(bill.date);
         dueDate.setDate(dueDate.getDate() + 30);
         
         const row = document.createElement('tr');
         row.innerHTML = `
             <td>CT-${bill.id}</td>
             <td>${bill.customer}</td>
             <td>${bill.date}</td>
             <td>₹${bill.total.toFixed(2)}</td>
             <td>₹${bill.paid.toFixed(2)}</td>
             <td>₹${bill.pending.toFixed(2)}</td>
             <td>${dueDate.toISOString().split('T')[0]}</td>
             <td>
                 <span class="badge ${bill.status === 'Paid' ? 'badge-success' : bill.status === 'Partial' ? 'badge-warning' : 'badge-danger'}">
                     ${bill.status}
                 </span>
             </td>
             <td>
                 ${bill.pending > 0 ? 
                     `<button class="action-btn payment-btn" data-id="${bill.id}"><i class="fas fa-rupee-sign"></i></button>` : 
                     '<span class="badge badge-success">Paid</span>'
                 }
             </td>
         `;
         paymentsTableBody.appendChild(row);
     });
     
     // Add payment event listeners
     document.querySelectorAll('.payment-btn').forEach(btn => {
         btn.addEventListener('click', function() {
             const billId = parseInt(this.getAttribute('data-id'));
             openPaymentModal(billId);
         });
     });
 }
 
 function renderBills() {
     billsTableBody.innerHTML = '';
     
     if (bills.length === 0) {
         billsTableBody.innerHTML = `
             <tr>
                 <td colspan="7" class="empty-state">
                     <i class="fas fa-file-invoice"></i>
                     <p>No bills generated yet. Create your first bill!</p>
                 </td>
             </tr>
         `;
         return;
     }
     
     bills.forEach(bill => {
         const row = document.createElement('tr');
         row.innerHTML = `
             <td>CT-${bill.id}</td>
             <td>${bill.date}</td>
             <td>${bill.customer}</td>
             <td>₹${bill.total.toFixed(2)}</td>
             <td>₹${bill.paid.toFixed(2)}</td>
             <td>₹${bill.pending.toFixed(2)}</td>
             <td>
                 <span class="badge ${bill.status === 'Paid' ? 'badge-success' : bill.status === 'Partial' ? 'badge-warning' : 'badge-danger'}">
                     ${bill.status}
                 </span>
             </td>
         `;
         billsTableBody.appendChild(row);
     });
 }
 
 function openPaymentModal(billId) {
     const bill = bills.find(b => b.id === billId);
     if (!bill) return;
     
     currentPaymentBill = bill;
     
     document.getElementById('payment-bill-no').value = `CT-${bill.id}`;
     document.getElementById('payment-customer').value = bill.customer;
     document.getElementById('payment-total').value = bill.total.toFixed(2);
     document.getElementById('payment-paid').value = bill.paid.toFixed(2);
     document.getElementById('payment-pending').value = bill.pending.toFixed(2);
     document.getElementById('payment-amount').value = '';
     document.getElementById('payment-date').valueAsDate = new Date();
     document.getElementById('payment-notes').value = '';
     
     paymentModal.style.display = 'flex';
 }
 
 function closePaymentModal() {
     paymentModal.style.display = 'none';
     currentPaymentBill = null;
 }
 
 function savePayment() {
     const paymentAmount = parseFloat(document.getElementById('payment-amount').value);
     const paymentDate = document.getElementById('payment-date').value;
     
     if (!paymentAmount || paymentAmount <= 0 || !paymentDate) {
         showToast('Please enter a valid payment amount and date', 'error');
         return;
     }
     
     if (paymentAmount > currentPaymentBill.pending) {
         showToast(`Payment amount cannot exceed pending amount of ₹${currentPaymentBill.pending.toFixed(2)}`, 'error');
         return;
     }
     
     // Update bill
     currentPaymentBill.paid += paymentAmount;
     currentPaymentBill.pending = currentPaymentBill.total - currentPaymentBill.paid;
     currentPaymentBill.status = currentPaymentBill.pending === 0 ? 'Paid' : 'Partial';
     
     // Save to localStorage
     localStorage.setItem('chathurBills', JSON.stringify(bills));
     
     // Close modal and update UI
     closePaymentModal();
     renderPayments();
     renderBills();
     updateDashboard();
     showToast('Payment recorded successfully!');
 }
 
 function updateDashboard() {
     // Update product count
     document.getElementById('total-products').textContent = inventory.length;
     
     // Update monthly sales
     const currentMonth = new Date().toISOString().slice(0, 7);
     const monthlySales = bills
         .filter(bill => bill.date.includes(currentMonth))
         .reduce((sum, bill) => sum + bill.total, 0);
     document.getElementById('monthly-sales').textContent = monthlySales.toLocaleString('en-IN');
     
     // Update pending payments
     const pendingPayments = bills.reduce((sum, bill) => sum + bill.pending, 0);
     document.getElementById('pending-payments').textContent = pendingPayments.toLocaleString('en-IN');
     
     // Update recent transactions
     recentTransactionsBody.innerHTML = '';
     const recentBills = [...bills].sort((a, b) => new Date(b.date) - new Date(a.date)).slice(0, 5);
     
     if (recentBills.length === 0) {
         recentTransactionsBody.innerHTML = `
             <tr>
                 <td colspan="5" class="empty-state">
                     <i class="fas fa-exchange-alt"></i>
                     <p>No recent transactions</p>
                 </td>
             </tr>
         `;
         return;
     }
     
     recentBills.forEach(bill => {
         const row = document.createElement('tr');
         row.innerHTML = `
             <td>CT-${bill.id}</td>
             <td>${bill.customer}</td>
             <td>${bill.date}</td>
             <td>₹${bill.total.toFixed(2)}</td>
             <td>
                 <span class="badge ${bill.status === 'Paid' ? 'badge-success' : bill.status === 'Partial' ? 'badge-warning' : 'badge-danger'}">
                     ${bill.status}
                 </span>
             </td>
         `;
         recentTransactionsBody.appendChild(row);
     });
 }
 
 function showToast(message, type = 'success') {
     const toast = document.getElementById('toast');
     toast.textContent = message;
     toast.className = `toast show ${type}`;
     
     setTimeout(() => {
         toast.className = 'toast';
     }, 3000);
 }