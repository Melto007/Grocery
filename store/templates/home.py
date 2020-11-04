{% extends 'main_header.py' %}

{% block content %}
<body>
	<!-- top-header -->
	<div class="header-most-top">
		<p>Grocery Offer Zone Top Deals & Discounts</p>
	</div>
	<!-- //top-header -->
	<!-- header-bot-->
	<div class="header-bot">
		<div class="header-bot_inner_wthreeinfo_header_mid">
			<!-- header-bot-->
			<div class="col-md-4 logo_agile">
				<h1>
					<a href="index.html">
						<span>G</span>rocery
						<span>S</span>hoppy
						<img src="images/logo2.png" alt=" ">
					</a>
				</h1>
			</div>
			<!-- header-bot -->
			<div class="col-md-8 header">
				<!-- header lists -->
				<ul>
					<li>
						<a class="play-icon popup-with-zoom-anim" href="#small-dialog1">
							<span class="fa fa-map-marker" aria-hidden="true"></span> Shop Locator</a>
					</li>
					<li>
						<a href="#" data-toggle="modal" data-target="#myModal1">
							<span class="fa fa-truck" aria-hidden="true"></span>Track Order</a>
					</li>
					<li>
						<span class="fa fa-phone" aria-hidden="true"></span> 001 234 5678
					</li>
					<li>
						<a href="#" data-toggle="modal" data-target="#myModal1">
							<span class="fa fa-unlock-alt" aria-hidden="true"></span> Sign In </a>
					</li>
					<li>
						<a href="#" data-toggle="modal" data-target="#myModal2">
							<span class="fa fa-pencil-square-o" aria-hidden="true"></span> Sign Up </a>
					</li>
				</ul>
				<!-- //header lists -->
				<!-- search -->
				<div class="agileits_search">
					<form action="#" method="post">
						<input name="Search" type="search" placeholder="How can we help you today?" required="">
						<button type="submit" class="btn btn-default" aria-label="Left Align">
							<span class="fa fa-search" aria-hidden="true"> </span>
						</button>
					</form>
				</div>
				<!-- //search -->
				<!-- cart details -->
				<div class="top_nav_right">
					<div class="wthreecartaits wthreecartaits2 cart cart box_1">
						<form action="#" method="post" class="last">
							<input type="hidden" name="cmd" value="_cart">
							<input type="hidden" name="display" value="1">
							<button class="w3view-cart" type="submit" name="submit" value="">
								<i class="fa fa-cart-arrow-down" aria-hidden="true"></i>
							</button>
						</form>
					</div>
				</div>
				<!-- //cart details -->
				<div class="clearfix"></div>
			</div>
			<div class="clearfix"></div>
		</div>
	</div>
	<!-- shop locator (popup) -->
	<!-- Button trigger modal(shop-locator) -->
	<div id="small-dialog1" class="mfp-hide">
		<div class="select-city">
			<h3>Please Select Your Location</h3>
			<select class="list_of_cities">
				<optgroup label="Popular Cities">
					<option selected style="display:none;color:#eee;">Select City</option>
					<option>Birmingham</option>
					<option>Anchorage</option>
					<option>Phoenix</option>
					<option>Little Rock</option>
					<option>Los Angeles</option>
					<option>Denver</option>
					<option>Bridgeport</option>
					<option>Wilmington</option>
					<option>Jacksonville</option>
					<option>Atlanta</option>
					<option>Honolulu</option>
					<option>Boise</option>
					<option>Chicago</option>
					<option>Indianapolis</option>
				</optgroup>
				<optgroup label="Alabama">
					<option>Birmingham</option>
					<option>Montgomery</option>
					<option>Mobile</option>
					<option>Huntsville</option>
					<option>Tuscaloosa</option>
				</optgroup>
				<optgroup label="Alaska">
					<option>Anchorage</option>
					<option>Fairbanks</option>
					<option>Juneau</option>
					<option>Sitka</option>
					<option>Ketchikan</option>
				</optgroup>
				<optgroup label="Arizona">
					<option>Phoenix</option>
					<option>Tucson</option>
					<option>Mesa</option>
					<option>Chandler</option>
					<option>Glendale</option>
				</optgroup>
				<optgroup label="Arkansas">
					<option>Little Rock</option>
					<option>Fort Smith</option>
					<option>Fayetteville</option>
					<option>Springdale</option>
					<option>Jonesboro</option>
				</optgroup>
				<optgroup label="California">
					<option>Los Angeles</option>
					<option>San Diego</option>
					<option>San Jose</option>
					<option>San Francisco</option>
					<option>Fresno</option>
				</optgroup>
				<optgroup label="Colorado">
					<option>Denver</option>
					<option>Colorado</option>
					<option>Aurora</option>
					<option>Fort Collins</option>
					<option>Lakewood</option>
				</optgroup>
				<optgroup label="Connecticut">
					<option>Bridgeport</option>
					<option>New Haven</option>
					<option>Hartford</option>
					<option>Stamford</option>
					<option>Waterbury</option>
				</optgroup>
				<optgroup label="Delaware">
					<option>Wilmington</option>
					<option>Dover</option>
					<option>Newark</option>
					<option>Bear</option>
					<option>Middletown</option>
				</optgroup>
				<optgroup label="Florida">
					<option>Jacksonville</option>
					<option>Miami</option>
					<option>Tampa</option>
					<option>St. Petersburg</option>
					<option>Orlando</option>
				</optgroup>
				<optgroup label="Georgia">
					<option>Atlanta</option>
					<option>Augusta</option>
					<option>Columbus</option>
					<option>Savannah</option>
					<option>Athens</option>
				</optgroup>
				<optgroup label="Hawaii">
					<option>Honolulu</option>
					<option>Pearl City</option>
					<option>Hilo</option>
					<option>Kailua</option>
					<option>Waipahu</option>
				</optgroup>
				<optgroup label="Idaho">
					<option>Boise</option>
					<option>Nampa</option>
					<option>Meridian</option>
					<option>Idaho Falls</option>
					<option>Pocatello</option>
				</optgroup>
				<optgroup label="Illinois">
					<option>Chicago</option>
					<option>Aurora</option>
					<option>Rockford</option>
					<option>Joliet</option>
					<option>Naperville</option>
				</optgroup>
				<optgroup label="Indiana">
					<option>Indianapolis</option>
					<option>Fort Wayne</option>
					<option>Evansville</option>
					<option>South Bend</option>
					<option>Hammond</option>														       
				</optgroup>
				<optgroup label="Iowa">
					<option>Des Moines</option>
					<option>Cedar Rapids</option>
					<option>Davenport</option>
					<option>Sioux City</option>
					<option>Waterloo</option>       													
				</optgroup>
				<optgroup label="Kansas">
					<option>Wichita</option>
					<option>Overland Park</option>
					<option>Kansas City</option>
					<option>Topeka</option>
					<option>Olathe  </option>            													
				</optgroup>
				<optgroup label="Kentucky">
					<option>Louisville</option>
					<option>Lexington</option>
					<option>Bowling Green</option>
					<option>Owensboro</option>
					<option>Covington</option>        														
				</optgroup>
				<optgroup label="Louisiana">
					<option>New Orleans</option>
					<option>Baton Rouge</option>
					<option>Shreveport</option>
					<option>Metairie</option>
					<option>Lafayette</option>          														
				</optgroup>
				<optgroup label="Maine">
					<option>Portland</option>
					<option>Lewiston</option>
					<option>Bangor</option>
					<option>South Portland</option>
					<option>Auburn</option>         														
				</optgroup>
				<optgroup label="Maryland">
					<option>Baltimore</option>
					<option>Frederick</option>
					<option>Rockville</option>
					<option>Gaithersburg</option>
					<option>Bowie</option>         														
				</optgroup>
				<optgroup label="Massachusetts">
					<option>Boston</option>
					<option>Worcester</option>
					<option>Springfield</option>
					<option>Lowell</option>
					<option>Cambridge</option>  
				</optgroup>
				<optgroup label="Michigan">
					<option>Detroit</option>
					<option>Grand Rapids</option>
					<option>Warren</option>
					<option>Sterling Heights</option>
					<option>Lansing</option> 
				</optgroup>
				<optgroup label="Minnesota">
					<option>Minneapolis</option>
					<option>St. Paul</option>
					<option>Rochester</option>
					<option>Duluth</option>
					<option>Bloomington</option>      														
				</optgroup>
				<optgroup label="Mississippi">
					<option>Jackson</option>
					<option>Gulfport</option>
					<option>Southaven</option>
					<option>Hattiesburg</option>
					<option>Biloxi</option>         														
				</optgroup>
				<optgroup label="Missouri">
					<option>Kansas City</option>
					<option>St. Louis</option>
					<option>Springfield</option>
					<option>Independence</option>
					<option>Columbia</option>            														
				</optgroup>
				<optgroup label="Montana">
					<option>Billings</option>
					<option>Missoula</option>
					<option>Great Falls</option>
					<option>Bozeman</option>
					<option>Butte-Silver Bow</option>         														
				</optgroup>
				<optgroup label="Nebraska">
					<option>Omaha</option>
					<option>Lincoln</option>
					<option>Bellevue</option>
					<option>Grand Island</option>
					<option>Kearney</option>        													
				</optgroup>
				<optgroup label="Nevada">
					<option>Las Vegas</option>
					<option>Henderson</option>
					<option>North Las Vegas</option>
					<option>Reno</option>
					<option>Sunrise Manor</option>            													
				</optgroup>
				<optgroup label="New Hampshire">
					<option>Manchesters</option>
					<option>Nashua</option>
					<option>Concord</option>
					<option>Dover</option>
					<option>Rochester</option>              													
				</optgroup>
				<optgroup label="New Jersey">
					<option>Newark</option>
					<option>Jersey City</option>
					<option>Paterson</option>
					<option>Elizabeth</option>
					<option>Edison</option> 
				</optgroup>
				<optgroup label="New Mexico">
					<option>Albuquerque</option>
					<option>Las Cruces</option>
					<option>Rio Rancho</option>
					<option>Santa Fe</option>
					<option>Roswell</option>       
				</optgroup>
				<optgroup label="New York">
					<option>New York</option>
					<option>Buffalo</option>
					<option>Rochester</option>
					<option>Yonkers</option>
					<option>Syracuse</option>        														
				</optgroup>
				<optgroup label="North Carolina">
					<option>Charlotte</option>
					<option>Raleigh</option>
					<option>Greensboro</option>
					<option>Winston-Salem</option>
					<option>Durham</option>          														
				</optgroup>
				<optgroup label="North Dakota">
					<option>Fargo</option>
					<option>Bismarck</option>
					<option>Grand Forks</option>
					<option>Minot</option>
					<option>West Fargo</option>
				</optgroup>
				<optgroup label="Ohio">
					<option>Columbus</option>
					<option>Cleveland</option>
					<option>Cincinnati</option>
					<option>Toledo</option>
					<option>Akron</option>      
				</optgroup>
				<optgroup label="Oklahoma">
					<option>Oklahoma City</option>
					<option>Tulsa</option>
					<option>Norman</option>
					<option>Broken Arrow</option>
					<option>Lawton</option>        														
				</optgroup>
				<optgroup label="Oregon">
					<option>Portland</option>
					<option>Eugene</option>
					<option>Salem</option>
					<option>Gresham</option>
					<option>Hillsboro</option>          														
				</optgroup>
				<optgroup label="Pennsylvania">
					<option>Philadelphia</option>
					<option>Pittsburgh</option>
					<option>Allentown</option>
					<option>Erie</option>
					<option>Reading</option>         														
				</optgroup>
				<optgroup label="Rhode Island">
					<option>Providence</option>
					<option>Warwick</option>
					<option>Cranston</option>
					<option>Pawtucket</option>
					<option>East Providence</option>   
				</optgroup>
				<optgroup label="South Carolina">
					<option>Columbia</option>
					<option>Charleston</option>
					<option>North Charleston</option>
					<option>Mount Pleasant</option>
					<option>Rock Hill</option> 
				</optgroup>
				<optgroup label="South Dakota">
					<option>Sioux Falls</option>
					<option>Rapid City</option>
					<option>Aberdeen</option>
					<option>Brookings</option>
					<option>Watertown</option> 
				</optgroup>
				<optgroup label="Tennessee">
					<option>Memphis</option>
					<option>Nashville</option>
					<option>Knoxville</option>
					<option>Chattanooga</option>
					<option>Clarksville</option>       
				</optgroup>
				<optgroup label="Texas">
					<option>Houston</option>
					<option>San Antonio</option>
					<option>Dallas</option>
					<option>Austin</option>
					<option>Fort Worth</option>   
				</optgroup>
				<optgroup label="Utah">
					<option>Salt Lake City</option>
					<option>West Valley City</option>
					<option>Provo</option>
					<option>West Jordan</option>
					<option>Orem</option>   
				</optgroup>	
				<optgroup label="Vermont">
					<option>Burlington</option>
					<option>Essex</option>
					<option>South Burlington</option>
					<option>Colchester</option>
					<option>Rutland</option>   
				</optgroup>
				<optgroup label="Virginia">
					<option>Virginia Beach</option>
					<option>Norfolk</option>
					<option>Chesapeake</option>
					<option>Arlington</option>
					<option>Richmond</option> 
				</optgroup>	
				<optgroup label="Washington">
					<option>Seattle</option>
					<option>Spokane</option>
					<option>Tacoma</option>
					<option>Vancouver</option>
					<option>Bellevue</option> 
				</optgroup>	
				<optgroup label="West Virginia">
					<option>Charleston</option>
					<option>Huntington</option>
					<option>Parkersburg</option>
					<option>Morgantown</option>
					<option>Wheeling</option> 
				</optgroup>	
				<optgroup label="Wisconsin">
					<option>Milwaukee</option>
					<option>Madison</option>
					<option>Green Bay</option>
					<option>Kenosha</option>
					<option>Racine</option>
				</optgroup>
				<optgroup label="Wyoming">
					<option>Cheyenne</option>
					<option>Casper</option>
					<option>Laramie</option>
					<option>Gillette</option>
					<option>Rock Springs</option>
				</optgroup>
			</select>
			<div class="clearfix"></div>
		</div>
	</div>
	<!-- //shop locator (popup) -->
	<!-- signin Model -->
	<!-- Modal1 -->
	<div class="modal fade" id="myModal1" tabindex="-1" role="dialog">
		<div class="modal-dialog">
			<!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
				</div>
				<div class="modal-body modal-body-sub_agile">
					<div class="main-mailposi">
						<span class="fa fa-envelope-o" aria-hidden="true"></span>
					</div>
					<div class="modal_body_left modal_body_left1">
						<h3 class="agileinfo_sign">Sign In </h3>
						<p>
							Sign In now, Let's start your Grocery Shopping. Don't have an account?
							<a href="#" data-toggle="modal" data-target="#myModal2">
								Sign Up Now</a>
						</p>
						<form action="#" method="post">
							<div class="styled-input agile-styled-input-top">
								<input type="text" placeholder="User Name" name="Name" required="">
							</div>
							<div class="styled-input">
								<input type="password" placeholder="Password" name="password" required="">
							</div>
							<input type="submit" value="Sign In">
						</form>
						<div class="clearfix"></div>
					</div>
					<div class="clearfix"></div>
				</div>
			</div>
			<!-- //Modal content-->
		</div>
	</div>
	<!-- //Modal1 -->
	<!-- //signin Model -->
	<!-- signup Model -->
	<!-- Modal2 -->
	<div class="modal fade" id="myModal2" tabindex="-1" role="dialog">
		<div class="modal-dialog">
			<!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
				</div>
				<div class="modal-body modal-body-sub_agile">
					<div class="main-mailposi">
						<span class="fa fa-envelope-o" aria-hidden="true"></span>
					</div>
					<div class="modal_body_left modal_body_left1">
						<h3 class="agileinfo_sign">Sign Up</h3>
						<p>
							Come join the Grocery Shoppy! Let's set up your Account.
						</p>
						<form action="#" method="post">
							<div class="styled-input agile-styled-input-top">
								<input type="text" placeholder="Name" name="Name" required="">
							</div>
							<div class="styled-input">
								<input type="email" placeholder="E-mail" name="Email" required="">
							</div>
							<div class="styled-input">
								<input type="password" placeholder="Password" name="password" id="password1" required="">
							</div>
							<div class="styled-input">
								<input type="password" placeholder="Confirm Password" name="Confirm Password" id="password2" required="">
							</div>
							<input type="submit" value="Sign Up">
						</form>
						<p>
							<a href="#">By clicking register, I agree to your terms</a>
						</p>
					</div>
				</div>
			</div>
			<!-- //Modal content-->
		</div>
	</div>
	<!-- //Modal2 -->
	<!-- //signup Model -->
	<!-- //header-bot -->
	<!-- navigation -->
	<div class="ban-top">
		<div class="container">
			<div class="agileits-navi_search">
				<form action="#" method="post">
					<select id="agileinfo-nav_search" name="agileinfo_search" required="">
						<option value="">All Categories</option>
						<option value="Kitchen">Kitchen</option>
						<option value="Household">Household</option>
						<option value="Snacks &amp; Beverages">Snacks & Beverages</option>
						<option value="Personal Care">Personal Care</option>
						<option value="Gift Hampers">Gift Hampers</option>
						<option value="Fruits &amp; Vegetables">Fruits & Vegetables</option>
						<option value="Baby Care">Baby Care</option>
						<option value="Soft Drinks &amp; Juices">Soft Drinks & Juices</option>
						<option value="Frozen Food">Frozen Food</option>
						<option value="Bread &amp; Bakery">Bread & Bakery</option>
						<option value="Sweets">Sweets</option>
					</select>
				</form>
			</div>
			<div class="top_nav_left">
				<nav class="navbar navbar-default">
					<div class="container-fluid">
						<!-- Brand and toggle get grouped for better mobile display -->
						<div class="navbar-header">
							<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
							    aria-expanded="false">
								<span class="sr-only">Toggle navigation</span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
							</button>
						</div>
						<!-- Collect the nav links, forms, and other content for toggling -->
						<div class="collapse navbar-collapse menu--shylock" id="bs-example-navbar-collapse-1">
							<ul class="nav navbar-nav menu__list">
								<li class="active">
									<a class="nav-stylehead" href="index.html">Home
										<span class="sr-only">(current)</span>
									</a>
								</li>
								<li class="">
									<a class="nav-stylehead" href="about.html">About Us</a>
								</li>
								<li class="dropdown">
									<a href="#" class="dropdown-toggle nav-stylehead" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Kitchen
										<span class="caret"></span>
									</a>
									<ul class="dropdown-menu multi-column columns-3">
										<div class="agile_inner_drop_nav_info">
											<div class="col-sm-4 multi-gd-img">
												<ul class="multi-column-dropdown">
													<li>
														<a href="product.html">Bakery</a>
													</li>
													<li>
														<a href="product.html">Baking Supplies</a>
													</li>
													<li>
														<a href="product.html">Coffee, Tea & Beverages</a>
													</li>
													<li>
														<a href="product.html">Dried Fruits, Nuts</a>
													</li>
													<li>
														<a href="product.html">Sweets, Chocolate</a>
													</li>
													<li>
														<a href="product.html">Spices & Masalas</a>
													</li>
													<li>
														<a href="product.html">Jams, Honey & Spreads</a>
													</li>
												</ul>
											</div>
											<div class="col-sm-4 multi-gd-img">
												<ul class="multi-column-dropdown">
													<li>
														<a href="product.html">Pickles</a>
													</li>
													<li>
														<a href="product.html">Pasta & Noodles</a>
													</li>
													<li>
														<a href="product.html">Rice, Flour & Pulses</a>
													</li>
													<li>
														<a href="product.html">Sauces & Cooking Pastes</a>
													</li>
													<li>
														<a href="product.html">Snack Foods</a>
													</li>
													<li>
														<a href="product.html">Oils, Vinegars</a>
													</li>
													<li>
														<a href="product.html">Meat, Poultry & Seafood</a>
													</li>
												</ul>
											</div>
											<div class="col-sm-4 multi-gd-img">
												<img src="images/nav.png" alt="">
											</div>
											<div class="clearfix"></div>
										</div>
									</ul>
								</li>
								<li class="dropdown">
									<a href="#" class="dropdown-toggle nav-stylehead" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Household
										<span class="caret"></span>
									</a>
									<ul class="dropdown-menu multi-column columns-3">
										<div class="agile_inner_drop_nav_info">
											<div class="col-sm-6 multi-gd-img">
												<ul class="multi-column-dropdown">
													<li>
														<a href="product2.html">Kitchen & Dining</a>
													</li>
													<li>
														<a href="product2.html">Detergents</a>
													</li>
													<li>
														<a href="product2.html">Utensil Cleaners</a>
													</li>
													<li>
														<a href="product2.html">Floor & Other Cleaners</a>
													</li>
													<li>
														<a href="product2.html">Disposables, Garbage Bag</a>
													</li>
													<li>
														<a href="product2.html">Repellents & Fresheners</a>
													</li>
													<li>
														<a href="product2.html"> Dishwash</a>
													</li>
												</ul>
											</div>
											<div class="col-sm-6 multi-gd-img">
												<ul class="multi-column-dropdown">
													<li>
														<a href="product2.html">Pet Care</a>
													</li>
													<li>
														<a href="product2.html">Cleaning Accessories</a>
													</li>
													<li>
														<a href="product2.html">Pooja Needs</a>
													</li>
													<li>
														<a href="product2.html">Crackers</a>
													</li>
													<li>
														<a href="product2.html">Festive Decoratives</a>
													</li>
													<li>
														<a href="product2.html">Plasticware</a>
													</li>
													<li>
														<a href="product2.html">Home Care</a>
													</li>
												</ul>
											</div>
											<div class="clearfix"></div>
										</div>
									</ul>
								</li>
								<li class="">
									<a class="nav-stylehead" href="faqs.html">Faqs</a>
								</li>
								<li class="dropdown">
									<a class="nav-stylehead dropdown-toggle" href="#" data-toggle="dropdown">Pages
										<b class="caret"></b>
									</a>
									<ul class="dropdown-menu agile_short_dropdown">
										<li>
											<a href="icons.html">Web Icons</a>
										</li>
										<li>
											<a href="typography.html">Typography</a>
										</li>
									</ul>
								</li>
								<li class="">
									<a class="nav-stylehead" href="contact.html">Contact</a>
								</li>
							</ul>
						</div>
					</div>
				</nav>
			</div>
		</div>
	</div>
	<!-- //navigation -->
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
				<!-- price range -->
				<div class="range">
					<h3 class="agileits-sear-head">Price range</h3>
					<ul class="dropdown-menu6">
						<li>

							<div id="slider-range"></div>
							<input type="text" id="amount" style="border: 0; color: #ffffff; font-weight: normal;" />
						</li>
					</ul>
				</div>
				<!-- //price range -->
				<!-- food preference -->
				<div class="left-side">
					<h3 class="agileits-sear-head">Food Preference</h3>
					<ul>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Vegetarian</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Non-Vegetarian</span>
						</li>
					</ul>
				</div>
				<!-- //food preference -->
				<!-- discounts -->
				<div class="left-side">
					<h3 class="agileits-sear-head">Discount</h3>
					<ul>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">5% or More</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">10% or More</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">20% or More</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">30% or More</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">50% or More</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">60% or More</span>
						</li>
					</ul>
				</div>
				<!-- //discounts -->
				<!-- reviews -->
				<div class="customer-rev left-side">
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
				</div>
				<!-- //reviews -->
				<!-- cuisine -->
				<div class="left-side">
					<h3 class="agileits-sear-head">Cuisine</h3>
					<ul>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">South American</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">French</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Greek</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Chinese</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Japanese</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Italian</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Mexican</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Thai</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span">Indian</span>
						</li>
						<li>
							<input type="checkbox" class="checked">
							<span class="span"> Spanish </span>
						</li>
					</ul>
				</div>
				<!-- //cuisine -->
				<!-- deals -->
				<div class="deal-leftmk left-side">
					<h3 class="agileits-sear-head">Special Deals</h3>
					<div class="special-sec1">
						<div class="col-xs-4 img-deals">
							<img src="images/d2.jpg" alt="">
						</div>
						<div class="col-xs-8 img-deal1">
							<h3>Lay's Potato Chips</h3>
							<a href="single.html">$18.00</a>
						</div>
						<div class="clearfix"></div>
					</div>
					<div class="special-sec1">
						<div class="col-xs-4 img-deals">
							<img src="images/d1.jpg" alt="">
						</div>
						<div class="col-xs-8 img-deal1">
							<h3>Bingo Mad Angles</h3>
							<a href="single.html">$9.00</a>
						</div>
						<div class="clearfix"></div>
					</div>
					<div class="special-sec1">
						<div class="col-xs-4 img-deals">
							<img src="images/d4.jpg" alt="">
						</div>
						<div class="col-xs-8 img-deal1">
							<h3>Tata Salt</h3>
							<a href="single.html">$15.00</a>
						</div>
						<div class="clearfix"></div>
					</div>
					<div class="special-sec1">
						<div class="col-xs-4 img-deals">
							<img src="images/d5.jpg" alt="">
						</div>
						<div class="col-xs-8 img-deal1">
							<h3>Gujarat Dry Fruit</h3>
							<a href="single.html">$525.00</a>
						</div>
						<div class="clearfix"></div>
					</div>
					<div class="special-sec1">
						<div class="col-xs-4 img-deals">
							<img src="images/d3.jpg" alt="">
						</div>
						<div class="col-xs-8 img-deal1">
							<h3>Cadbury Dairy Milk</h3>
							<a href="single.html">$149.00</a>
						</div>
						<div class="clearfix"></div>
					</div>
				</div>
				<!-- //deals -->
			</div>
			<!-- //product left -->
			<!-- product right -->
			<div class="agileinfo-ads-display col-md-9">
				<div class="wrapper">
					<!-- first section (nuts) -->
					<div class="product-sec1">
						<h3 class="heading-tittle">Nuts</h3>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/m1.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<span class="product-new-top">New</span>
								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Almonds, 100g</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$149.00</span>
										<del>$280.00</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="Almonds, 100g" />
												<input type="hidden" name="amount" value="149.00" />
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
						</div>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/m2.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<span class="product-new-top">New</span>

								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Cashew Nuts, 100g</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$200.00</span>
										<del>$420.00</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="Cashew Nuts, 100g" />
												<input type="hidden" name="amount" value="200.00" />
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
						</div>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/m3.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<span class="product-new-top">New</span>

								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Pista..., 250g</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$520.99</span>
										<del>$600.99</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="Pista, 250g" />
												<input type="hidden" name="amount" value="520.99" />
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
						</div>
						<div class="clearfix"></div>
					</div>
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
					<div class="product-sec1">
						<h3 class="heading-tittle">Oils</h3>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/mk4.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<span class="product-new-top">New</span>
								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Freedom Oil, 1L</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$78.00</span>
										<del>$110.00</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="Freedom Sunflower Oil, 1L" />
												<input type="hidden" name="amount" value="78.00" />
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
						</div>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/mk5.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<span class="product-new-top">New</span>

								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Saffola Gold, 1L</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$130.00</span>
										<del>$150.00</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="Saffola Gold, 1L" />
												<input type="hidden" name="amount" value="130.00" />
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
						</div>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/mk6.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<span class="product-new-top">New</span>

								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Fortune Oil, 5L</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$399.99</span>
										<del>$500.00</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="Fortune Oil, 5L" />
												<input type="hidden" name="amount" value="399.99" />
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
						</div>
						<div class="clearfix"></div>
					</div>
					<!-- //third section (oils) -->
					<!-- fourth section (noodles) -->
					<div class="product-sec1">
						<h3 class="heading-tittle">Pasta & Noodles</h3>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/mk7.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Yippee Noodles, 65g</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$15.00</span>
										<del>$25.00</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="YiPPee Noodles, 65g" />
												<input type="hidden" name="amount" value="15.00" />
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
						</div>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/mk8.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<span class="product-new-top">New</span>

								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Wheat Pasta, 500g</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$98.00</span>
										<del>$120.00</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="Wheat Pasta, 500g" />
												<input type="hidden" name="amount" value="98.00" />
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
						</div>
						<div class="col-md-4 product-men">
							<div class="men-pro-item simpleCart_shelfItem">
								<div class="men-thumb-item">
									<img src="images/mk9.jpg" alt="">
									<div class="men-cart-pro">
										<div class="inner-men-cart-pro">
											<a href="single.html" class="link-product-add-cart">Quick View</a>
										</div>
									</div>
									<span class="product-new-top">New</span>

								</div>
								<div class="item-info-product ">
									<h4>
										<a href="single.html">Chinese Noodles, 68g</a>
									</h4>
									<div class="info-product-price">
										<span class="item_price">$11.99</span>
										<del>$15.00</del>
									</div>
									<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
										<form action="#" method="post">
											<fieldset>
												<input type="hidden" name="cmd" value="_cart" />
												<input type="hidden" name="add" value="1" />
												<input type="hidden" name="business" value=" " />
												<input type="hidden" name="item_name" value="Chinese Noodles, 68g" />
												<input type="hidden" name="amount" value="11.99" />
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
						</div>
						<div class="clearfix"></div>
					</div>
					<!-- //fourth section (noodles) -->
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