{% extends 'main_header.py' %}

{% block content %}
<body>

	<style>
		.pagination a {
		color: black;
		float: left;
		padding: 8px 16px;
		text-decoration: none;
		transition: background-color .3s;
		}

		.pagination a.active {
		background-color: dodgerblue;
		color: white;
		}

		.pagination a:hover:not(.active) {background-color: #ddd;}
	</style>
	
	<!-- banner -->
	<div id="myCarousel" class="carousel slide" data-ride="carousel">
		<!-- Indicators-->
		<ol class="carousel-indicators">
			<li data-target="#myCarousel" data-slide-to="0" class="active"></li>
			<li data-target="#myCarousel" data-slide-to="1" class=""></li>
			<li data-target="#myCarousel" data-slide-to="2" class=""></li>
			<li data-target="#myCarousel" data-slide-to="3" class=""></li>
		</ol>
		<div class="carousel-inner" role="listbox">
			<div class="item active">
				<div class="container">
					<div class="carousel-caption">
						<h3>Big
							<span>Save</span>
						</h3>
						<p>Get flat
							<span>10%</span> Cashback</p>
						<a class="button2" href="product.html">Shop Now </a>
					</div>
				</div>
			</div>
			<div class="item item2">
				<div class="container">
					<div class="carousel-caption">
						<h3>Healthy
							<span>Saving</span>
						</h3>
						<p>Get Upto
							<span>30%</span> Off</p>
						<a class="button2" href="product.html">Shop Now </a>
					</div>
				</div>
			</div>
			<div class="item item3">
				<div class="container">
					<div class="carousel-caption">
						<h3>Big
							<span>Deal</span>
						</h3>
						<p>Get Best Offer Upto
							<span>20%</span>
						</p>
						<a class="button2" href="product.html">Shop Now </a>
					</div>
				</div>
			</div>
			<div class="item item4">
				<div class="container">
					<div class="carousel-caption">
						<h3>Today
							<span>Discount</span>
						</h3>
						<p>Get Now
							<span>40%</span> Discount</p>
						<a class="button2" href="product.html">Shop Now </a>
					</div>
				</div>
			</div>
		</div>
		<a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
			<span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
			<span class="sr-only">Previous</span>
		</a>
		<a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
			<span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
			<span class="sr-only">Next</span>
		</a>
	</div>
	<!-- //banner -->

	<!-- top Products -->
	<div class="ads-grid">
		<div class="container">
			<!-- tittle heading -->
			<h3 class="tittle-w3l">Our Top Products
				<span class="heading-style">
					<i></i>
					<i></i>
					<i></i>
				</span>
			</h3>
			<!-- //tittle heading -->
			<!-- product left -->
			<div class="side-bar col-md-3">
				<div class="search-hotel">
					<h3 class="agileits-sear-head">Search Here..</h3>
					<form action="#" method="post">
						<input type="search" placeholder="Product name..." name="search" required="">
						<input type="submit" value=" ">
					</form>
				</div>

		<form action='{% url "cat_selection" %}' method='post'>
			{% csrf_token %}
				<!-- food preference -->
				<div class="left-side">
					<h3 class="agileits-sear-head">Food Preference</h3>
					<ul>
						<li>
							<input type="radio" name="food" class="checked" value="Vegetarian" required>
							<span class="span">Vegetarian</span>
						</li>
						<li>
							<input type="radio" name="food" class="checked" class="Non-Vegetarian" required>
							<span class="span">Non-Vegetarian</span>
						</li>
						<li>
							<input type="radio" name="food" class="checked" value="Other" required>
							<span class="span">Other</span>
						</li>
					</ul>
				</div>
				<!-- //food preference -->
				<!-- discounts -->
				<div class="left-side">
					<h3 class="agileits-sear-head">Discount</h3>
					<ul>
						<li>
							<input type="radio" name="discount" value="30" class="checked" required>
							<span class="span">5% or More</span>
						</li>
						<li>
							<input type="radio"  name="discount" class="checked" required>
							<span class="span">10% or More</span>
						</li>
						<li>
							<input type="radio" name="discount" class="checked" required>
							<span class="span">20% or More</span>
						</li>
						<li>
							<input type="radio" name="discount" class="checked" required>
							<span class="span">30% or More</span>
						</li>
						<li>
							<input type="radio" name="discount" class="checked" required>
							<span class="span">50% or More</span>
						</li>
						<li>
							<input type="radio" name="discount" class="checked" required>
							<span class="span">60% or More</span>
						</li>
					</ul>
				</div>
				<!-- //discounts -->
				<!-- reviews -->
			<!--	<div class="customer-rev left-side">
					<h3 class="agileits-sear-head">Customer Review</h3>
					<ul>
						<li>
							<a href="#">
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<span>5.0</span>
							</a>
						</li>
						<li>
							<a href="#">
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star-o" aria-hidden="true"></i>
								<span>4.0</span>
							</a>
						</li>
						<li>
							<a href="#">
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star-half-o" aria-hidden="true"></i>
								<i class="fa fa-star-o" aria-hidden="true"></i>
								<span>3.5</span>
							</a>
						</li>
						<li>
							<a href="#">
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star-o" aria-hidden="true"></i>
								<i class="fa fa-star-o" aria-hidden="true"></i>
								<span>3.0</span>
							</a>
						</li>
						<li>
							<a href="#">
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star" aria-hidden="true"></i>
								<i class="fa fa-star-half-o" aria-hidden="true"></i>
								<i class="fa fa-star-o" aria-hidden="true"></i>
								<i class="fa fa-star-o" aria-hidden="true"></i>
								<span>2.5</span>
							</a>
						</li>
					</ul>
				</div> -->
				<!-- //reviews -->
				<!-- cuisine -->
				<div class="left-side">
					<h3 class="agileits-sear-head">Cuisine</h3>
					<ul>
						{% for cuisine in cuisine %}
							<li>
								<input type="radio" class="checked" name="cuisine" value={{ cuisine.id }} required>
								<span class="span">{{ cuisine.cuisine_name }}</span>
							</li>
						{% endfor %}
					</ul>
				</div>
				<!-- //cuisine -->
				<!-- deals -->
				<div class="deal-leftmk left-side">
					<div class="special-sec1">
						<div class="col-xs-12 img-deals">
							<button class='btn btn-primary' type='submit'>Search</button>
						</div>
						<div class="clearfix"></div>
					</div>
				</div>
				<!-- //deals -->
			</div>
		</form>

			<!-- //product left -->
			<!-- product right -->
			
			<div class="agileinfo-ads-display col-md-9">
				<div class="wrapper">
				
					<!-- //first section (nuts) -->
					<!-- second section (nuts special) -->
					<div class="product-sec1 product-sec2">
						<div class="col-xs-7 effect-bg">
							<h3 class="">Pure Energy</h3>
							<h6>Enjoy our all healthy Products</h6>
							<p>Get Extra 10% Off</p>
						</div>
						<h3 class="w3l-nut-middle">Nuts & Dry Fruits</h3>
						<div class="col-xs-5 bg-right-nut">
							<img src="images/nut1.png" alt="">
						</div>
						<div class="clearfix"></div>
					</div>
					<!-- //second section (nuts special) -->
					<!-- third section (oils) -->
			<!--- //Pagination --->
				<div class="pagination">
						<a href="#">&laquo;</a>
					{% for num in product.paginator.page_range %}
						{% if product.number == num%}
							<a class="active" href="#"><strong>{{ num }}</strong></a>
						{% elif num > product.number|add:'-3' and num < product.number|add:'3' %}
							<a href="?page={{ num }}">{{ num }}</a>
						{% endif %}
					{% endfor %}
					<a href="#">&laquo;</a>
				</div>
			<!---// Pagination --->
					<div class="product-sec1">
						<h3 class="heading-tittle">Products</h3>	

					{% if view_product %}
						{% for view_product in view_product %}
						<div class="col-md-4 product-men">
						
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="{{ view_product.imageURL }}" width="200px" height="175px" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<!--<span class="product-new-top">New</span> -->
								</div>
								<div class="item-info-product ">
									<h4>
										<a href="">{{ view_product.name }}</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">${{ view_product.price }}</span>
										<del>${{ view_product.discount }}</del>
									</div>
							
								<form action='{% url 'update_item' %}' method='POST'>
									{% csrf_token %}
									<input type="hidden" name='userid' value='{{ user.id }}'>
									<input type='hidden' name='product' value='{{ view_product.id }}'>
									
									<button type='submit' class='btn btn-success'>Add to Cart</button>
								</form>

								</div>
								
							</div>
						</div>
						{% endfor %}
					{% else %}
						{% for product in product %}
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="{{ product.imageURL }}" width="200px" height="175px" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<!--<span class="product-new-top">New</span> -->
								</div>
								<div class="item-info-product ">
									<h4>
										<a href="">{{ product.name }}</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">${{ product.price }}</span>
										<del>${{ product.discount }}</del>
									</div>
							
								<form action='{% url 'update_item' %}' method='POST'>
									{% csrf_token %}
									<input type="hidden" name='userid' value='{{ user.id }}'>
									<input type='hidden' name='product' value='{{ product.id }}'>
									
									<button type='submit' class='btn btn-success'>Add to Cart</button>
								</form>

								</div>
							</div>
						</div>
						{% endfor %}
					{% endif %}

						<div class="clearfix"></div>
					</div>
					<!-- //third section (oils) -->
				</div>
			</div>
			<!-- //product right -->
		</div>
	</div>

	<!-- //top products -->
	<!-- special offers -->
	<div class="featured-section" id="projects">
		<div class="container">
			<!-- tittle heading -->
			<h3 class="tittle-w3l">Special Offers
				<span class="heading-style">
					<i></i>
					<i></i>
					<i></i>
				</span>
			</h3>
			<!-- //tittle heading -->
			<div class="content-bottom-in">
				<ul id="flexiselDemo1">
					<li>
						<div class="w3l-specilamk">
							<div class="speioffer-agile">
								<a href="single.html">
									<img src="images/s1.jpg" alt="">
								</a>
							</div>
							<div class="product-name-w3l">
								<h4>
									<a href="single.html">Aashirvaad, 5g</a>
								</h4>
								<div class="w3l-pricehkj">
									<h6>$220.00</h6>
									<p>Save $40.00</p>
								</div>
								<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
									<form action="#" method="post">
										<fieldset>
											<input type="hidden" name="cmd" value="_cart" />
											<input type="hidden" name="add" value="1" />
											<input type="hidden" name="business" value=" " />
											<input type="hidden" name="item_name" value="Aashirvaad, 5g" />
											<input type="hidden" name="amount" value="220.00" />
											<input type="hidden" name="discount_amount" value="1.00" />
											<input type="hidden" name="currency_code" value="USD" />
											<input type="hidden" name="return" value=" " />
											<input type="hidden" name="cancel_return" value=" " />
											<input type="submit" name="submit" value="Add to cart" class="button" />
										</fieldset>
									</form>
								</div>
							</div>
						</div>
					</li>
					<li>
						<div class="w3l-specilamk">
							<div class="speioffer-agile">
								<a href="single.html">
									<img src="images/s4.jpg" alt="">
								</a>
							</div>
							<div class="product-name-w3l">
								<h4>
									<a href="single.html">Kissan Tomato Ketchup, 950g</a>
								</h4>
								<div class="w3l-pricehkj">
									<h6>$99.00</h6>
									<p>Save $20.00</p>
								</div>
								<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
									<form action="#" method="post">
										<fieldset>
											<input type="hidden" name="cmd" value="_cart" />
											<input type="hidden" name="add" value="1" />
											<input type="hidden" name="business" value=" " />
											<input type="hidden" name="item_name" value="Kissan Tomato Ketchup, 950g" />
											<input type="hidden" name="amount" value="99.00" />
											<input type="hidden" name="discount_amount" value="1.00" />
											<input type="hidden" name="currency_code" value="USD" />
											<input type="hidden" name="return" value=" " />
											<input type="hidden" name="cancel_return" value=" " />
											<input type="submit" name="submit" value="Add to cart" class="button" />
										</fieldset>
									</form>
								</div>
							</div>
						</div>
					</li>
					<li>
						<div class="w3l-specilamk">
							<div class="speioffer-agile">
								<a href="single.html">
									<img src="images/s2.jpg" alt="">
								</a>
							</div>
							<div class="product-name-w3l">
								<h4>
									<a href="single.html">Madhur Pure Sugar, 1g</a>
								</h4>
								<div class="w3l-pricehkj">
									<h6>$69.00</h6>
									<p>Save $20.00</p>
								</div>
								<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
									<form action="#" method="post">
										<fieldset>
											<input type="hidden" name="cmd" value="_cart" />
											<input type="hidden" name="add" value="1" />
											<input type="hidden" name="business" value=" " />
											<input type="hidden" name="item_name" value="Madhur Pure Sugar, 1g" />
											<input type="hidden" name="amount" value="69.00" />
											<input type="hidden" name="discount_amount" value="1.00" />
											<input type="hidden" name="currency_code" value="USD" />
											<input type="hidden" name="return" value=" " />
											<input type="hidden" name="cancel_return" value=" " />
											<input type="submit" name="submit" value="Add to cart" class="button" />
										</fieldset>
									</form>
								</div>
							</div>
						</div>
					</li>
					<li>
						<div class="w3l-specilamk">
							<div class="speioffer-agile">
								<a href="single2.html">
									<img src="images/s3.jpg" alt="">
								</a>
							</div>
							<div class="product-name-w3l">
								<h4>
									<a href="single2.html">Surf Excel Liquid, 1.02L</a>
								</h4>
								<div class="w3l-pricehkj">
									<h6>$187.00</h6>
									<p>Save $30.00</p>
								</div>
								<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
									<form action="#" method="post">
										<fieldset>
											<input type="hidden" name="cmd" value="_cart" />
											<input type="hidden" name="add" value="1" />
											<input type="hidden" name="business" value=" " />
											<input type="hidden" name="item_name" value="Surf Excel Liquid, 1.02L" />
											<input type="hidden" name="amount" value="187.00" />
											<input type="hidden" name="discount_amount" value="1.00" />
											<input type="hidden" name="currency_code" value="USD" />
											<input type="hidden" name="return" value=" " />
											<input type="hidden" name="cancel_return" value=" " />
											<input type="submit" name="submit" value="Add to cart" class="button" />
										</fieldset>
									</form>
								</div>
							</div>
						</div>
					</li>
					<li>
						<div class="w3l-specilamk">
							<div class="speioffer-agile">
								<a href="single.html">
									<img src="images/s8.jpg" alt="">
								</a>
							</div>
							<div class="product-name-w3l">
								<h4>
									<a href="single.html">Cadbury Choclairs, 655.5g</a>
								</h4>
								<div class="w3l-pricehkj">
									<h6>$160.00</h6>
									<p>Save $60.00</p>
								</div>
								<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
									<form action="#" method="post">
										<fieldset>
											<input type="hidden" name="cmd" value="_cart" />
											<input type="hidden" name="add" value="1" />
											<input type="hidden" name="business" value=" " />
											<input type="hidden" name="item_name" value="Cadbury Choclairs, 655.5g" />
											<input type="hidden" name="amount" value="160.00" />
											<input type="hidden" name="discount_amount" value="1.00" />
											<input type="hidden" name="currency_code" value="USD" />
											<input type="hidden" name="return" value=" " />
											<input type="hidden" name="cancel_return" value=" " />
											<input type="submit" name="submit" value="Add to cart" class="button" />
										</fieldset>
									</form>
								</div>
							</div>
						</div>
					</li>
					<li>
						<div class="w3l-specilamk">
							<div class="speioffer-agile">
								<a href="single2.html">
									<img src="images/s6.jpg" alt="">
								</a>
							</div>
							<div class="product-name-w3l">
								<h4>
									<a href="single2.html">Fair & Lovely, 80 g</a>
								</h4>
								<div class="w3l-pricehkj">
									<h6>$121.60</h6>
									<p>Save $30.00</p>
								</div>
								<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
									<form action="#" method="post">
										<fieldset>
											<input type="hidden" name="cmd" value="_cart" />
											<input type="hidden" name="add" value="1" />
											<input type="hidden" name="business" value=" " />
											<input type="hidden" name="item_name" value="Fair & Lovely, 80 g" />
											<input type="hidden" name="amount" value="121.60" />
											<input type="hidden" name="discount_amount" value="1.00" />
											<input type="hidden" name="currency_code" value="USD" />
											<input type="hidden" name="return" value=" " />
											<input type="hidden" name="cancel_return" value=" " />
											<input type="submit" name="submit" value="Add to cart" class="button" />
										</fieldset>
									</form>
								</div>
							</div>
						</div>
					</li>
					<li>
						<div class="w3l-specilamk">
							<div class="speioffer-agile">
								<a href="single.html">
									<img src="images/s5.jpg" alt="">
								</a>
							</div>
							<div class="product-name-w3l">
								<h4>
									<a href="single.html">Sprite, 2.25L (Pack of 2)</a>
								</h4>
								<div class="w3l-pricehkj">
									<h6>$180.00</h6>
									<p>Save $30.00</p>
								</div>
								<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
									<form action="#" method="post">
										<fieldset>
											<input type="hidden" name="cmd" value="_cart" />
											<input type="hidden" name="add" value="1" />
											<input type="hidden" name="business" value=" " />
											<input type="hidden" name="item_name" value="Sprite, 2.25L (Pack of 2)" />
											<input type="hidden" name="amount" value="180.00" />
											<input type="hidden" name="discount_amount" value="1.00" />
											<input type="hidden" name="currency_code" value="USD" />
											<input type="hidden" name="return" value=" " />
											<input type="hidden" name="cancel_return" value=" " />
											<input type="submit" name="submit" value="Add to cart" class="button" />
										</fieldset>
									</form>
								</div>
							</div>
						</div>
					</li>
					<li>
						<div class="w3l-specilamk">
							<div class="speioffer-agile">
								<a href="single2.html">
									<img src="images/s9.jpg" alt="">
								</a>
							</div>
							<div class="product-name-w3l">
								<h4>
									<a href="single2.html">Lakme Eyeconic Kajal, 0.35 g</a>
								</h4>
								<div class="w3l-pricehkj">
									<h6>$153.00</h6>
									<p>Save $40.00</p>
								</div>
								<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
									<form action="#" method="post">
										<fieldset>
											<input type="hidden" name="cmd" value="_cart" />
											<input type="hidden" name="add" value="1" />
											<input type="hidden" name="business" value=" " />
											<input type="hidden" name="item_name" value="Lakme Eyeconic Kajal, 0.35 g" />
											<input type="hidden" name="amount" value="153.00" />
											<input type="hidden" name="discount_amount" value="1.00" />
											<input type="hidden" name="currency_code" value="USD" />
											<input type="hidden" name="return" value=" " />
											<input type="hidden" name="cancel_return" value=" " />
											<input type="submit" name="submit" value="Add to cart" class="button" />
										</fieldset>
									</form>
								</div>
							</div>
						</div>
					</li>
				</ul>
			</div>
		</div>
	</div>
	<!-- //special offers -->
	<!-- newsletter -->
	<div class="footer-top">
		<div class="container-fluid">
			<div class="col-xs-8 agile-leftmk">
				<h2>Get your Groceries delivered from local stores</h2>
				<p>Free Delivery on your first order!</p>
				<form action="#" method="post">
					<input type="email" placeholder="E-mail" name="email" required="">
					<input type="submit" value="Subscribe">
				</form>
				<div class="newsform-w3l">
					<span class="fa fa-envelope-o" aria-hidden="true"></span>
				</div>
			</div>
			<div class="col-xs-4 w3l-rightmk">
				<img src="images/tab3.png" alt=" ">
			</div>
			<div class="clearfix"></div>
		</div>
	</div>
	<!-- //newsletter -->

{% endblock %}