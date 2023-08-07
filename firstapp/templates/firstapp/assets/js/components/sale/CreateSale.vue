<template>
  <div>
    <h1>Submit JSON Form</h1>
    <form @submit.prevent="submitForm" id="jsonForm">
      <label for="phone">Phone:</label>
      <input
        type="text"
        id="phone"
        name="phone"
        v-model="formData.phone" /><br />

      <label for="date">Date:</label>
      <input type="date" id="date" name="date" v-model="formData.date" /><br />

      <label for="status">Status:</label>
      <input
        type="number"
        id="status"
        name="status"
        v-model="formData.status" /><br />

      <label for="payment_status">Payment Status:</label>
      <input
        type="number"
        id="payment_status"
        name="payment_status"
        v-model="formData.payment_status" /><br />

      <label for="total_quantity">Total Quantity:</label>
      <input
        type="number"
        id="total_quantity"
        name="total_quantity"
        v-model="formData.total_quantity" /><br />

      <label for="total">Total:</label>
      <input
        type="number"
        step="0.01"
        id="total"
        name="total"
        v-model="formData.total" /><br />

      <label for="discount">Discount:</label>
      <input
        type="number"
        step="0.01"
        id="discount"
        name="discount"
        v-model="formData.discount" /><br />

      <label for="shipping_cost">Shipping Cost:</label>
      <input
        type="number"
        step="0.01"
        id="shipping_cost"
        name="shipping_cost"
        v-model="formData.shipping_cost" /><br />

      <label for="grand_total">Grand Total:</label>
      <input
        type="number"
        step="0.01"
        id="grand_total"
        name="grand_total"
        v-model="formData.grand_total" /><br />

      <label for="paid">Paid:</label>
      <input
        type="number"
        step="0.01"
        id="paid"
        name="paid"
        v-model="formData.paid" /><br />

      <label for="due">Due:</label>
      <input
        type="number"
        step="0.01"
        id="due"
        name="due"
        v-model="formData.due" /><br />

      <label for="note">Note:</label>
      <textarea id="note" name="note" v-model="formData.note"></textarea><br />

      <!-- Supplier Field (ForeignKey) -->
      <label for="customer">Customer:</label>
      <select id="customer" name="customer" v-model="formData.customer">
        <option value="">Select a customer</option>
        <option value="1">one customer</option>
        <option value="2">2 customer</option></select
      ><br />

      <hr />

      <label for="sale_order_product">Sale Order Products:</label>

      <div v-for="(product, index) in saleOrderProducts" :key="index">
        <div>
          <label for="quantity">Quantity:</label>
          <input
            type="number"
            class="classToValidate"
            v-model="product.quantity"
            :name="'sale_order_product_quantity' + product.id" /><br />

          <!-- Product Field (ForeignKey) -->
          <label for="product">Product:</label>
          <select
            id="product"
            class="classToValidate"
            v-model="product.product"
            :name="'purchase_order_product_product' + product.id">
            <option value="">Select a product</option>
            <option value="1">one product</option>
            <option value="2">2 product</option></select
          ><br />

          <label for="sub_total">Sub Total:</label>
          <input
            type="number"
            class="classToValidate"
            step="0.01"
            v-model="product.sub_total"
            :name="'sale_order_product_sub_total' + product.id" /><br />

          <br />
        </div>
      </div>

      <button type="button" @click="addProductField">Add Product</button><br />

      <button type="submit">Submit JSON</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        phone: null,
        date: null,
        status: null,
        payment_status: null,
        total_quantity: null,
        total: null,
        discount: null,
        shipping_cost: null,
        grand_total: null,
        paid: null,
        due: null,
        note: null,
        customer: null,
      },
      counter_saleOrderProducts: 0,
      saleOrderProducts: [],
    };
  },
  methods: {
    addProductField() {
      this.counter_saleOrderProducts++;
      this.saleOrderProducts.push({
        quantity: null,
        product: null,
        sub_total: null,
        id: this.counter_saleOrderProducts,
      });
    },
    submitForm() {
      const formData = { ...this.formData };
      if (this.saleOrderProducts.length === 0) {
        alert("Please enter products");
        return;
      }
      formData.sale_order_product = this.saleOrderProducts;

      console.log(JSON.stringify(formData));

      // axios
      //   .post("http://127.0.0.1:8000/api/sales/create/", formData, {
      //     headers: {
      //       "Content-Type": "application/json",
      //     },
      //   })
      //   .then((response) => {
      //     console.log("Successfully submitted:", response.data);
      //   })
      //   .catch((error) => {
      //     console.log("Error submitting form:", error.response.data);
      //   });
    },
  },
};
</script>
