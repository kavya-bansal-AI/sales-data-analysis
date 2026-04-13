import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("train.csv")
print(df.head())
print(df.info())
print(df.columns)

Sales_by_Category= df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(Sales_by_Category)
Sales_by_Category.plot(kind='bar')
plt.title("Sales_by_Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head()
print(top_products)
top_products.plot(kind='bar')
plt.title("Top 5 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.show()

df['Profit']=df['Sales']*df['Category'].map({
    'Furniture':0.1,
    'Technology': 0.2,
    'Office Supplies':0.25
})
Profit_by_category=df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print(Profit_by_category)

print("sales_by_category:")
print(Sales_by_Category)
print("\n profit_by_category:")
print(Profit_by_category)

combined= pd.DataFrame({
    'sales':Sales_by_Category,
    'profit':Profit_by_category
})
print(combined)

combined.plot(kind='bar')
plt.title('sales vs profit by category')
plt.xlabel('category')
plt.ylabel('values')
plt.show()

print('\n____MENU____')
print('1. sales_by_category' )
print('2. top_products')
print('3. profit_by_category')
print('4. Filter by Category')

choice= input('enter your choice: 1/2/3')

if choice == '1':
    print(Sales_by_Category)
    Sales_by_Category.plot(kind='bar')
    plt.title('Sales_by_category')
    plt.xlabel('category')
    plt.ylabel('sales')
    plt.show()

elif choice == '2':
    print(top_products) 
    top_products.plot(kind='bar')  
    plt.title('top_products')
    plt.xlabel('sub_category')
    plt.ylabel('sales')
    plt.show()

elif choice == '3':
    print(Profit_by_category) 
    Profit_by_category.plot(kind='bar')  
    plt.title('profit_by_category')
    plt.xlabel('ctaegory')
    plt.ylabel('profit')
    plt.show()

elif choice == "4":
    cat = input("Enter category (Furniture/Technology/Office Supplies): ")
    filtered = df[df["Category"] == cat]
    print(filtered.head())
    filtered.groupby("Sub-Category")["Sales"].sum().plot(kind='bar')
    plt.title(f"Sales in {cat}")
    plt.xlabel("Sub-Category")
    plt.ylabel("Sales")
    plt.show()

else:
    print("Invalid choice")

combined.to_csv("sales and profit analysis.csv")

top_products.to_csv("top_products.csv")