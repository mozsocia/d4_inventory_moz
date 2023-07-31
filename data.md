## Puschase 


Sure, here's an example of a JSON payload for creating multiple `Purchase` objects along with their corresponding `Purchase_order_product` data:

```json
{
  "purchases": [
    {
      "phone": 1234567890,
      "date": "2023-07-27",
      "status": 1,
      "payment_status": 2,
      "total_quantity": 5,
      "total": 100.0,
      "discount": 10.0,
      "shipping_cost": 5.0,
      "grand_total": 95.0,
      "paid": 50.0,
      "due": 45.0,
      "note": "Sample note for purchase 1",
      "unit": 1,
      "supplier": 2,
      "category": 3,
      "brand": 4,
      "purchase_order_product": [
        {
          "sub_total": 50.0,
          "quantity": 2,
          "product": 1
        },
        {
          "sub_total": 45.0,
          "quantity": 3,
          "product": 2
        }
      ]
    },
    {
      "phone": 9876543210,
      "date": "2023-07-28",
      "status": 1,
      "payment_status": 1,
      "total_quantity": 3,
      "total": 50.0,
      "grand_total": 50.0,
      "paid": 50.0,
      "note": "Sample note for purchase 2",
      "unit": 2,
      "supplier": 3,
      "category": 4,
      "brand": 5,
      "purchase_order_product": [
        {
          "sub_total": 30.0,
          "quantity": 1,
          "product": 3
        },
        {
          "sub_total": 20.0,
          "quantity": 2,
          "product": 4
        }
      ]
    }
  ]
}
```

In the above JSON payload, we are sending data for two `Purchase` objects. Each object has its attributes along with an array of `Purchase_order_product` objects, representing the products associated with that purchase. Replace the sample data with the actual data you want to create. Note that the `unit`, `supplier`, `category`, and `brand` fields refer to the primary keys of their respective models.



## customer
Sure! Here's an example array containing two JSON data objects that you can use for POST requests:

```json
[
  {
    "name": "John Doe",
    "customer_ID": "CUST123",
    "address": "123 Main Street",
    "phone": 1234567890,
    "email": "john@example.com",
    "start_date": "2023-07-31",
    "image": "base64_encoded_image_data_1",
    "Created_at": "2023-07-31T12:00:00",
    "Updated_at": "2023-07-31T12:00:00"
  },
  {
    "name": "Jane Smith",
    "customer_ID": "CUST456",
    "address": "456 Park Avenue",
    "phone": 9876543210,
    "email": "jane@example.com",
    "start_date": "2023-07-30",
    "image": "base64_encoded_image_data_2",
    "Created_at": "2023-07-30T12:00:00",
    "Updated_at": "2023-07-30T12:00:00"
  }
]
```

Please note that the `image` field contains placeholder text "base64_encoded_image_data_1" and "base64_encoded_image_data_2". In practice, you would replace these with actual base64-encoded image data for each customer's image. Base64 encoding is commonly used when handling image uploads in JSON data. If you are using HTML forms for image uploads, you don't need to base64 encode the image, and Django will handle it automatically.


## Sale
Sure, here's an example of JSON data for the `POST` request to create a `Sale` along with an array of `Sale_order_product` data:

```json
{
  "phone": 1234567890,
  "date": "2023-07-30",
  "status": 1,
  "payment_status": 2,
  "total_quantity": 5,
  "total": 200.0,
  "discount": 10.0,
  "shipping_cost": 5.0,
  "grand_total": 195.0,
  "paid": 195.0,
  "due": 0.0,
  "note": "Sample note for the sale",
  "customer": 1,
  "sale_order_product": [
    {
      "quantity": 2,
      "product": 1,
      "sub_total": 50.0
    },
    {
      "quantity": 3,
      "product": 2,
      "sub_total": 150.0
    }
  ]
}
```

Note that you need to replace the `phone`, `date`, `total_quantity`, `total`, `discount`, `shipping_cost`, `grand_total`, `paid`, `due`, `note`, and `customer` values with appropriate data specific to your use case. Also, the `product` field in each `Sale_order_product` item should be the primary key (ID) of the corresponding `Product` object you want to associate with the sale.