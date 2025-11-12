from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from . import db, login_manager
from .models import Product, User
from .countries import get_countries_list
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
    countries = get_countries_list()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        country = request.form.get("country", "India")
        phone = request.form.get("phone", "")
        address = request.form.get("address", "")
        
        if User.query.filter_by(email=email).first():
            flash("Email already exists", "error")
            return redirect(url_for("main.register"))
        
        u = User(email=email, country=country, phone=phone, address=address)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        flash("Account created. Please login.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", countries=countries)

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
        flash("Product added", "success")
        return redirect(url_for("main.index"))
    return render_template("new_product.html")

# User Profile
@main_bp.route("/profile", methods=["GET"])
@login_required
def profile():
    countries = get_countries_list()
    return render_template("profile.html", countries=countries)

@main_bp.route("/profile/update", methods=["POST"])
@login_required
def update_profile():
    current_user.country = request.form.get("country", current_user.country)
    current_user.phone = request.form.get("phone", current_user.phone)
    current_user.address = request.form.get("address", current_user.address)
    db.session.commit()
    flash("Profile updated successfully!", "success")
    return redirect(url_for("main.profile"))

from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
