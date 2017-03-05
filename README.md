# TopStock Backend (0.1.0)

A hackathon project where Alexa has a hand in picking stocks and making recommendations
This project uses the Quantopia API and Markit On Demand for it's stock market data.

This backend is written in Flask and hosted on Heroku, here is the planned documentation for the API
routes so Alexa can communicate with the Market.

PyStockPicker takes the general stocks and then we run a second layer of a Market Moving Average (Tactical Stock Analysis)

For the stocks of interest we run

'''

'''

## Functionality

This Backend is able to retrive Stock prices for a particular stock
Be able to recommend the best US based stock based off of some factors
Be able to recommend the highest performing stock based off of purchase velocity
Be able to buy/sell using Alexa as the interface

## Routes

The root url is `localhost:8080/Api/v0`

### /Quote

**URL**

* `/Quote`

    Method:
    `GET` 

*  **URL Params**

   Field: Symbol
   Type: String <- Ticker Symbol
   

 **Optional Params**

    /TopStock

    with optional Fields
    (Tech, Resources)

* **Success Response:**
  

  * **Code:** 200 <br />
    **Content:** 
    ```
    {
    "Name":"Apple Inc",
    "Symbol":"AAPL",
    "LastPrice":524.49,
    "Change":15.6,
    "ChangePercent":3.06549549018453,
    "Timestamp":"Wed Oct 23 13:39:19 UTC-06:00 2013",
    "High":52499,
    "Low":519.175,
    "Open":519.175 
    }
    ```
 
* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Ticker Not Found" }`

### /Topfive

Returns the top five suggested

**URL**

* `/Quote`

    Method:
    `GET` 

*  **URL Params**

   Field: Symbol
   Type: String <- Ticker Symbol

* **Success Response:**
  

  * **Code:** 200 <br />
    **Content:** 
    ```
    {
    "one":"Apple Inc",
    "Symbol-one":"AAPL",
    "LastPrice-one":524.49,
    "two":"Apple Inc",
    "Symbol-two":"AAPL",
    "LastPrice-two":524.49,
    "three":"Apple Inc",
    "Symbol-three":"AAPL",
    "LastPrice-three":524.49,
    "four":"Apple Inc",
    "Symbol-four":"AAPL",
    "LastPrice-four":524.49,
    "five":"Apple Inc",
    "Symbol-five":"AAPL",
    "LastPrice-five":524.49,
    }
    ```
 
* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 500 SERIVE DOWN <br />
    **Content:** `{ error : "No connection" }`


