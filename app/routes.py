from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from . import db, login_manager
from .models import Product, User
from flask_login import login_user, logout_user, login_required, current_user

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)

@main_bp.route("/product/<int:product_id>")
def product_detail(product_id):
    p = Product.query.get_or_404(product_id)
    return render_template("product.html", product=p)

# Simple register/login (very minimal)
@main_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if User.query.filter_by(email=email).first():
            flash("Email already exists")
            return redirect(url_for("main.register"))
        u = User(email=email)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        flash("Account created. Please login.")
        return redirect(url_for("main.login"))
    return render_template("register.html")

@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        u = User.query.filter_by(email=email).first()
        if u and u.check_password(password):
            login_user(u)
            return redirect(url_for("main.index"))
        flash("Invalid credentials")
    return render_template("login.html")

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

# Cart: session-based
@main_bp.route("/cart/add/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session["cart"] = cart
    flash("Added to cart")
    return redirect(url_for("main.index"))

@main_bp.route("/cart")
def view_cart():
    cart = session.get("cart", {})
    items = []
    total = 0.0
    for pid, qty in cart.items():
        p = Product.query.get(int(pid))
        if p:
            items.append({"product": p, "qty": qty, "subtotal": p.price * qty})
            total += p.price * qty
    return render_template("cart.html", items=items, total=total)

# Admin routes to create products (very simple, no auth check here — add later)
@main_bp.route("/admin/product/new", methods=["GET", "POST"])
def new_product():
    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        desc = request.form.get("description")
        p = Product(name=name, price=price, description=desc)
        db.session.add(p)
        db.session.commit()
        flash("Product added")
        return redirect(url_for("main.index"))
    return render_template("new_product.html")
from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
