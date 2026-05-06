import streamlit as st
import pandas as pd

st.set_page_config(page_title="$10M USDT → Business Cash", page_icon="💸", layout="wide")

def render_table(df): st.dataframe(df, use_container_width=True, hide_index=True)

# ─── Page 1: Home ──────────────────────────────────────────────────────────────
def page_home():
    st.title("💸 Get $10M USDT — Clean and Business-Ready")
    st.subheader("No KYC exchange. No capital gains. Turn USDT into cash or business spending power.")
    st.markdown("---")

    st.success("""
**You have $10M USDT.** The problem: USDT is fine, but businesses don't accept it. You need to turn it into cash or find businesses that DO take USDT directly.

**3 ways to get your USDT business-ready:**
    """)

    render_table(pd.DataFrame({
        "Method": [
            "🤝 P2P Marketplace — Sell USDT for cash",
            "💳 Borrow Against USDT — Get cash without selling",
            "🏪 Run a USDT-Accepting Business — Spend USDT directly",
        ],
        "What It Is": [
            "Match buyers who want USDT. Take spread. Get cash.",
            "Use USDT as collateral. Get USD. Keep the USDT.",
            "Business accepts USDT from customers. Pays vendors in USDT.",
        ],
        "Cash Out": ["$500K–2M+/mo", "$4–7M", "Self-sustaining"],
        "Tax Event": ["No", "No", "No"],
    }))

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    col1.metric("P2P Revenue", "$500K–2M+/mo", "at 1–5% spread")
    col2.metric("Loan Cash Out", "$4–7M", "in 48hrs")
    col3.metric("Business Model", "Self-sustaining", "USDT in, USDT out")

    st.markdown("---")

    st.info("**The key insight:** Your USDT is already clean. The issue isn't legality — it's conversion. You either (1) sell it for cash, (2) borrow against it, or (3) find businesses that take USDT directly. All 3 avoid KYC exchanges.")

# ─── Page 2: P2P ──────────────────────────────────────────────────────────────
def page_p2p():
    st.title("🤝 Sell USDT via P2P — Get Cash")
    st.subheader("Connect USDT buyers with USDT holders. Take the spread. No exchange.")
    st.markdown("---")

    st.success("""
**The model:**
- Someone has USD cash → wants USDT
- You connect them with a USDT holder
- Cash goes to you (minus your fee) → USDT moves to the buyer
- You never "sell" to an exchange. No capital gains event.
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    col1.metric("Your Fee", "1–5%", "per trade")
    col2.metric("$50M/mo vol", "$500K–2.5M", "monthly revenue")
    col3.metric("No KYC", "On P2P platform", "for you")

    st.markdown("---")

    st.subheader("How the Cash Flows")
    st.markdown("""
```
CASH BUYER          YOUR ESCROW           USDT SELLER
────────────────────────────────────────────────────────
Sends you $10.3K → [USDT held in      → Releases $10K
                      your escrow]        USDT to buyer
                   You: +$10K USDT      Seller: +$10K cash
                   (spread: $300)
```

**What you do:** Collect the spread. Your USDT pile stays the same size — you're not selling yours, you're facilitating others.
    """)

    st.markdown("---")

    st.subheader("Revenue Calculator")
    c1, c2 = st.columns(2)
    with c1:
        vol = st.number_input("Monthly Volume ($)", value=50_000_000, format="%d")
    with c2:
        fee = st.slider("Your Spread/Fee %", 0.5, 5.0, 2.0)

    rev = vol * fee / 100
    st.metric("Monthly Revenue", f"${rev:,.0f}", f"${rev*12:,.0f}/yr")

    st.markdown("---")

    st.subheader("How to Run It")
    render_table(pd.DataFrame({
        "Step": ["1. Use Binance P2P or NoOnes", "2. Post ads: 'I'm selling USDT at market rate'", "3. Match with buyer", "4. Buyer sends you cash (bank transfer / cash)", "5. Release USDT from escrow", "6. Pocket the spread"],
        "Cash Flow": ["Set up account", "No USDT needed from you", "Buyer pays you", "USDT in escrow", "USDT released", "Spread is profit"],
    }))

    st.markdown("---")

    st.subheader("Your USDT Position — What Actually Happens")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Your starting position:**
        - $10M USDT in your wallet
        - Want to convert to cash

        **What P2P does for you:**
        - You facilitate trades between buyers and sellers
        - You never sell your own USDT on an exchange
        - You earn a fee on each trade
        - Your $10M USDT stays in your wallet
        - Cash comes in as fees
        """)
    with col2:
        st.markdown("""
        **Why no tax event:**
        - You're not selling your USDT
        - You're charging a service fee
        - Revenue (fees) = ordinary income
        - No capital gains on USDT because you didn't sell it

        **The catch:**
        - You need USDT sellers to list on your platform
        - Without your own platform, you're just a trader
        - As a trader: you ARE selling USDT → taxable
        """)
    st.markdown("---")
    st.warning("⚠️ If you run P2P on Binance/NoOnes: you're a user, not an operator. Your trades ARE taxable events. To avoid tax: build your own platform (licensed) where you're a service provider, not a trader.")

# ─── Page 3: Loans ─────────────────────────────────────────────────────────────
def page_loans():
    st.title("💳 Borrow Against USDT — Get Cash Without Selling")
    st.subheader("Put up USDT as collateral. Get USD wire. Keep the USDT.")
    st.markdown("---")

    st.success("""
**IRS rule (confirmed):** Borrowing against crypto is NOT a taxable event.

You don't sell your USDT. You pledge it as collateral. The USD comes to you as a loan. Your USDT stays in your wallet.
    """)

    st.markdown("---")

    st.subheader("The Problem: Most Places Want BTC/ETH — Not USDT")

    st.markdown("""
**USDT is harder to borrow against than BTC/ETH.** Here's the reality:
    """)

    render_table(pd.DataFrame({
        "Collateral": ["BTC / ETH", "wstETH (staked ETH)", "USDC", "USDT"],
        "Easy to Borrow Against?": ["✅ Yes", "✅ Yes", "✅ Yes", "⚠️ Harder"],
        "Best Platforms": ["Ledn, Unchained, Aave", "Aave, Morpho, Spark", "Aave, Maple, Morpho", "Aave V3 (limited)"],
        "LTV": ["50%", "75%", "75–80%", "50–75%"],
        "Note": ["Most platforms support this", "Best DeFi option", "Mainstream option", "Fewer options, check first"],
    }))

    st.markdown("---")

    st.subheader("The Workaround — Convert USDT to wstETH, Then Borrow")

    st.markdown("""
**The strategy if you have USDT and want a loan with no tax event:**
    """)

    render_table(pd.DataFrame({
        "Step": ["1. Swap USDT → ETH on Uniswap/DEX", "2. Stake ETH → wstETH (Lido)", "3. Deposit wstETH on Aave V3", "4. Borrow USDC at 75% LTV", "5. Swap USDC → USD via P2P or card", "6. USD in your bank"],
        "Tax Event": ["⚠️ Possible (swap = taxable)", "No", "No", "No", "No", "No"],
        "Fee": ["~0.3% DEX fee", "Stake: ~10% of yield", "0%", "Variable APR", "1–2% P2P", "Wire: $0–25"],
        "Time": ["Minutes", "24hrs to activate", "Instant", "Instant", "Same day", "1–3 days"],
    }))

    st.markdown("---")

    st.warning("⚠️ **The swap problem:** Swapping USDT → ETH is a taxable event (selling USDT). To avoid this entirely: use P2P or borrow directly if your platform supports USDT collateral.")

    st.markdown("---")

    st.subheader("Best Options for USDT Collateral Loans")

    render_table(pd.DataFrame({
        "Platform": ["Aave V3 (USDT pool)", "Morpho Blue (USDC)", "Maple Finance", "CoinRabbit", "Nexo", "YouHodler"],
        "USDT as Collateral": ["✅ Yes", "⚠️ USDC only", "⚠️ USDC only", "✅ Yes", "✅ Yes", "✅ Yes"],
        "LTV": ["75–80%", "N/A", "N/A", "Up to 50%", "Up to 70%", "Up to 50%"],
        "APR": ["5–7%", "5–8%", "4.9%", "8–16%", "10–13%", "Up to 27%"],
        "Output": ["USDC", "USDC", "USDC", "USD wire", "USD wire", "USD wire"],
        "KYC": ["No (DeFi)", "No (DeFi)", "No (on-chain)", "Yes", "Yes", "Yes"],
    }))

    st.markdown("---")

    st.subheader("Calculator — USDT as Collateral")
    c1, c2, c3 = st.columns(3)
    with c1:
        collateral = st.number_input("USDT Collateral ($)", value=10_000_000, format="%d")
    with c2:
        ltv = st.slider("LTV %", 30, 80, 50)
    with c3:
        apr = st.slider("APR %", 5.0, 20.0, 7.0)

    borrowed = collateral * ltv / 100
    annual_int = borrowed * apr / 100

    st.metric("Cash (USDC/USDT)", f"${borrowed:,.0f}", f"at {ltv}% of ${collateral/1e6:.0f}M")
    st.metric("Annual Interest", f"${annual_int:,.0f}", f"${annual_int/12:,.0f}/month")

# ─── Page 4: USDT Business ────────────────────────────────────────────────────
def page_usdt_biz():
    st.title("🏪 Run a Business That Accepts USDT")
    st.subheader("Never convert USDT. Just run a business where USDT flows in and out.")
    st.markdown("---")

    st.success("""
**The idea:** You have $10M USDT. Instead of converting it — start a business that earns USDT from customers, pays vendors in USDT, and grows.

Your USDT is the seed capital. The business makes USDT. You never "cash out."
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    col1.metric("USDT In", "Revenue from customers", "USDT never converted")
    col2.metric("USDT Out", "Pay vendors/contractors", "Direct on-chain")
    col3.metric("Your Living", "Salary paid in USDT", "Stablecoin card or P2P")

    st.markdown("---")

    st.subheader("Business Models That Work With USDT Directly")

    render_table(pd.DataFrame({
        "Business": ["E-commerce (global)", "Import/Export", "Marketing Agency", "Software/SaaS", "Staffing/HR Agency", "Freelance Network", "Consulting"],
        "What You Do": [
            "Sell products globally, accept USDT",
            "Buy goods cheap in one country, sell in another",
            "Manage ad campaigns for crypto companies",
            "Build tools for crypto/DeFi users",
            "Place contractors globally, bill in USDT",
            "Connect freelancers to clients, take 10%",
            "Advisors for crypto funds/protocols",
        ],
        "Accepts USDT": ["✅", "✅", "✅", "✅", "✅", "✅", "✅"],
        "Pay Vendors in USDT": ["⚠️ Some", "✅", "✅", "✅", "✅", "✅", "✅"],
        "Revenue Potential": ["High", "Very High", "Medium", "High", "Medium", "Medium", "Medium"],
    }))

    st.markdown("---")

    st.subheader("The Cash Flow — How USDT Moves Through the Business")

    st.markdown("""
```
$10M USDT SEED CAPITAL
       ↓
BUSINESS INCORPORATED (LLC)
       ↓
Pay contractors/vendors → in USDT (no tax event)
       ↓
Earn revenue from customers → in USDT
       ↓
Pay yourself a salary → USDT to personal wallet
       ↓
Spend via crypto card (Bleap, RedotPay, Fizen)
   OR sell small amounts via P2P for living expenses
```
    """)

    st.markdown("---")

    st.subheader("How to Pay Yourself From a USDT Business")

    render_table(pd.DataFrame({
        "Method": ["Crypto Debit Card", "P2P small sells", "PayPal / Zelle via exchange", "Wise / Mercury bank", "Crypto payroll (Deel, Bitwage)"],
        "How": ["Bleap Mastercard, RedotPay", "Sell $5–20K/day via P2P", "Small KYC on-ramp", "Business account linked to USDT", "Employees paid in USDT/USDC"],
        "Fees": ["~1% conversion", "0.5–2% P2P spread", "1–2%", "1%", "1–2%"],
        "KYC": ["No", "No", "Yes (small)", "Business KYC", "No"],
        "Best For": ["Daily spending", "Monthly expenses", "One-time large", "Payroll", "Team salaries"],
    }))

    st.markdown("---")

    st.subheader("Crypto Cards That Convert USDT → Cash Automatically")

    render_table(pd.DataFrame({
        "Card": ["Bleap Mastercard", "RedotPay", "BitPay", "Crypto.com", "Bybit Card", "Wirex"],
        "Converts": ["USDT/USDC → USD", "USDT/USDC → USD", "BTC, ETH, USDC", "Multiple", "Multiple", "Multiple"],
        "Cashback": ["2% USDC", "Up to 5%", "1.5%", "Up to 10%", "Up to 10%", "Up to 8%"],
        "ATM Fees": ["Free up to $400/mo", "Low", "~$2.50", "Free tiered", "Free tiered", "~$2"],
        "No KYC": ["✅", "✅", "⚠️ Some", "⚠️ Yes", "✅", "⚠️ Yes"],
        "Note": ["Best for large spenders", "High cashback", "Established", "High staking req.", "No stake req.", "WXT token needed"],
    }))

    st.markdown("---")

    st.subheader("The Legal Structure")

    st.markdown("""
**How to own a USDT business properly:**
    """)

    render_table(pd.DataFrame({
        "Step": ["1. Form Wyoming / Delaware LLC", "2. Get EIN from IRS", "3. Open business bank account (crypto-friendly)", "4. Set up Mercury / Relay / Unit banking", "5. Receive USDT in business wallet (Gnosis Safe)", "6. Pay all expenses from business wallet", "7. Pay yourself as employee or dividend"],
        "Why": ["Privacy + flexibility", "Required for banking", "Required for payroll", "Crypto-friendly banks", "Multi-sig security", "Clean accounting", "Taxed as ordinary income"],
    }))

    st.markdown("---")

    st.subheader("$10M Business Plan — USDT Native")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Option A — E-commerce / Import-Export**

        - Use $5M USDT to buy goods wholesale
        - Ship to LATAM / Africa / Asia
        - Sell for cash or USDT
        - Mark up 20–40%
        - $1–2M/yr profit in USDT
        - No exchange. Pure trade.
        """)
    with col2:
        st.markdown("""
        **Option B — Marketing / Lead Gen Agency**

        - Use $2M USDT to run ad campaigns
        - Crypto companies pay in USDT for leads
        - Your margin: 20–30%
        - $500K–1M/yr net in USDT
        - Global team paid in USDT
        - No banking needed
        """)

    st.markdown("---")

    st.error("""
⚠️ **Key legal points:**

- **USDT as salary** — legal in most states if both parties agree
- **USDT for vendors** — legal if vendor agrees to accept it
- **Business bank account** — bank will want to know about crypto. Use crypto-friendly banks.
- **Tax on business income** — the business pays tax on profit. You pay yourself a salary. USDT doesn't make income tax-free.
- **No magic:** You're not avoiding taxes — you're avoiding capital gains on the USDT itself, since you never sold it.
    """)

# ─── Page 5: Fraud ─────────────────────────────────────────────────────────────
def page_fraud():
    st.title("⚠️ How Others Got Caught — $10M Cases")
    st.subheader("7 real cases. Learn what NOT to do.")
    st.markdown("---")

    cases = [
        ("Crypto Dispensers — $10M (Nov 2025)", "Ran cash-to-BTC ATMs. Allegedly laundered fraud proceeds.", "Plea of not guilty. Max 20 years.", "Chainalysis traced funds. Banks flagged deposits. FBI followed money through ATMs.", "Every ATM tx is on-chain. Every cash deposit is tracked."),
        ("Paxful Platform — $7.5M Fine (Dec 2025)", "14M user P2P platform. Shut down completely.", "Plead guilty to 3 federal counts.", "No MTL licenses in states. No KYC/AML. Willful blindness to scammers.", "You're responsible for what happens on your platform."),
        ("Samourai Wallet — $100M+ (2024–2025)", "Privacy wallet with mixing.", "CEO: 60 months. CPO: 48 months.", "Mixing = money laundering intent. Chainalysis traced patterns.", "Privacy tools in US = treated as money laundering."),
        ("Ronald Spektor — $16M (Dec 2025)", "23yo impersonated Coinbase support.", "Indicted by Brooklyn DA.", "Victims reported to FBI IC3. Wallets traced.", "Scam others = prison. Ignoring platform scams = same."),
        ("Tether Freezes — $700M+ (2025–2026)", "USDT issuer freezing funds linked to fraud.", "Ongoing.", "Tether freezes on DOJ request. Funds traced through wallets.", "Tether can freeze your USDT. Instantly. No warning."),
        ("Bitcoin ATM Fraud — $333M (2025)", "45,000 BTC ATMs in US. Scammers used them.", "Mass. sued Bitcoin Depot. $10M+ fraudulent txns.", "Bank deposits flagged. FBI traced victim payments → ATM accounts.", "Running cash-into-crypto = bank accounts are watched."),
        ("Operation Atlantic — 276 Arrests (May 2026)", "US + China + Canada coordinated crackdown.", "$701M seized.", "International law enforcement highly coordinated on crypto crime.", "At $10M you're visible. Get licensed."),
    ]

    for name, what, outcome, caught, lesson in cases:
        with st.expander(name):
            st.markdown(f"**What:** {what}")
            st.markdown(f"**Outcome:** {outcome}")
            st.markdown(f"**How caught:** {caught}")
            st.error(f"**Lesson:** {lesson}")

    st.markdown("---")

    st.subheader("How to NOT Be These Guys")
    render_table(pd.DataFrame({
        "Do": ["Get FinCEN MSB + state MTL", "Basic KYC (phone + ID)", "File SARs when suspicious", "Chainalysis KYT monitoring", "Clean banking", "Know source of funds"],
        "Don't": ["Run without licenses", "Ignore scam reports", "Large anonymous txns", "Touch stolen funds", "Skip AML compliance", "Assume offshore = safe"],
    }))

def page_spend():
    st.title("🛒 What to Buy With USDT")
    st.subheader("Real things you can spend USDT on right now. No conversion needed.")
    st.markdown("---")

    st.success("""
    **You have $10M USDT. What can you actually spend it on?**
    
    The answer: a LOT more than you think. Here's every category, from flights to real estate to payroll.
    """)

    st.markdown("---")

    # Categories
    categories = [
        ("✈️ Travel", "flights, hotels, 2M+ properties globally"),
        ("🏠 Real Estate", "homes, land, commercial property worldwide"),
        ("🚗 Cars & Vehicles", "new, used, luxury, boats, planes"),
        ("💻 Tech & Software", "SaaS, domains, hosting, VPNs"),
        ("💼 Business Services", "accounting, legal, marketing, PR"),
        ("🌍 Global Payroll", "contractors, employees, freelancers"),
        ("🎯 Advertising", "Meta ads, Google ads via crypto cards"),
        ("🥇 Precious Metals", "gold, silver, platinum"),
        ("🏥 Services", "medical tourism, dental, IVF"),
        ("📚 Education", "courses, certifications, universities"),
        ("🎮 Gaming & Subscriptions", "PlayStation, Steam, Netflix"),
        ("🎁 Gift Cards", "Amazon, Apple, Google, any brand"),
    ]

    cols = st.columns(3)
    for i, (cat, examples) in enumerate(categories):
        cols[i % 3].markdown(f"**{cat}**  \n{examples}")

    st.markdown("---")

    # Detailed breakdown
    st.subheader("🛒 What to Buy — Full List")

    render_table(pd.DataFrame({
        "Category": [
            "✈️ Travel",
            "🏠 Real Estate",
            "🚗 Vehicles",
            "💻 Software/Tech",
            "💼 Business Services",
            "🌍 Payroll",
            "🎯 Advertising",
            "🥇 Gold/Silver",
            "📦 Consumer Goods",
            "🏥 Medical",
            "🎁 Gift Cards",
            "⚡ Energy/Utilities",
        ],
        "What Exactly": [
            "Travala (2M+ hotels), AirBaltic, flights via Travala/PayBito",
            "RealOpen, Direct with sellers, Ferris Cars, luxury property worldwide",
            "Ferrari, Porsche, McLaren via intermediaries; AutoGravity",
            "Namecheap, Surfshark VPN, hosting, domain names",
            "Agencies, consultants, legal, accounting (direct negotiation)",
            "Bitwage, Deel, Remote, any international contractor",
            "Meta ads via Bleap/RedotPay cards; Google via Moon virtual cards",
            "SuisseGold (physical delivery), XAUT tokenized gold on Kraken",
            "Shopify (merchants accept), direct from manufacturers",
            "Medical tourism agencies, dental clinics, cosmetic surgery",
            "Bitrefill, CoinGate, Cryptorefills (100+ brands)",
            "Solar panels, energy bills in some countries",
        ],
        "How to Pay": [
            "Direct on platform",
            "Escrow converts USDT",
            "Intermediary converts",
            "Direct on website",
            "Bank transfer from USDT",
            "Bitwage / direct USDT",
            "Crypto debit card",
            "Direct via platform",
            "Direct or via card",
            "Direct negotiation",
            "Instant digital",
            "Direct in some regions",
        ],
        "Fees": [
            "0–2%",
            "0.5–2%",
            "1–3%",
            "0%",
            "0%",
            "0.5–2%",
            "1–2%",
            "1–3%",
            "1–2%",
            "0%",
            "1–5%",
            "0%",
        ],
    }))

    st.markdown("---")

    # Travel detail
    st.subheader("✈️ Travel — Where USDT Works Directly")
    render_table(pd.DataFrame({
        "Platform": ["Travala", "AirBaltic", "CheapAir", "BTCTrip", "CryptoVegas"],
        "What": ["2M+ hotels, flights, cars", "Direct flights", "Flights + hotels", "Flights", "Hotels + packages"],
        "USDT Accepted": ["✅ Direct", "✅ Direct", "✅ Direct", "✅ Direct", "✅ Direct"],
        "Note": ["Largest crypto travel platform", "Baltic flag carrier", "Since 2015", "Specialized", "Gaming/hospitality"],
    }))

    st.markdown("---")

    # Real estate
    st.subheader("🏠 Real Estate — Buy Property With USDT")
    st.markdown("""
    **The process:**
    1. Find property → negotiate price
    2. Use **RealOpen** or direct escrow service
    3. USDT converts to fiat at closing (for title/deed)
    4. No capital gains for YOU — you spent USDT, didn't sell for profit
    
    **Where it works:** LATAM, Caribbean, Middle East, Southeast Asia, Europe, US (via escrow)
    **Typical minimums:** $50K–$500K depending on property
    **Fees:** 0.5–2% on the transaction
    """)

    # Vehicles
    st.subheader("🚗 Cars, Boats, Planes — Luxury Assets")
    render_table(pd.DataFrame({
        "Asset": ["Luxury Cars", "Everyday Cars", "Boats/Yachts", "Planes (private)", "RVs / Campers"],
        "Where": ["Ferris Cars, intermediaries", "AutoGravity, CarAMoon", "Global yacht brokers", "GlobalAir, controllers", "Direct from dealers"],
        "USDT": ["✅ Via intermediary", "✅ Via intermediary", "✅ Direct negotiation", "✅ Direct negotiation", "✅ Direct"],
        "Min": ["$50K+", "$10K+", "$100K+", "$500K+", "$20K+"],
        "Note": ["Most dealers convert for you", "Growing acceptance", "Sellers prefer USDT in LATAM/MENA", "Common in private aviation", "Many US dealers accept"],
    }))

    st.markdown("---")

    # Payroll
    st.subheader("🌍 Payroll — Pay Anyone Globally With USDT")
    st.markdown("""
    **Best platforms for paying contractors/employees with USDT:**
    """)
    render_table(pd.DataFrame({
        "Platform": ["Bitwage", "Deel", "Remote", "Salarium", "Direct (Gnosis Safe)"],
        "What": ["Contractor payroll in USDT", "Full payroll + compliance", "Global payroll", "LATAM focused", "Manual USDT transfer"],
        "Fees": ["0.5–1%", "Free for employers", "Custom pricing", "Varies", "Network fee only"],
        "Employee Gets": ["USDT, USDC, or fiat", "Local bank or USDT", "Local bank or USDT", "Local bank", "USDT in wallet"],
    }))

    st.markdown("---")

    # Software
    st.subheader("💻 Software & Tech — USDT Direct")
    render_table(pd.DataFrame({
        "Service": ["Namecheap", "Surfshark VPN", "PrivateVPN", "Hostinger", "Hetzner", "Exodus Wallet"],
        "What": ["Domains + hosting", "VPN subscription", "VPN subscription", "Web hosting", "Servers", "Wallet"],
        "How": ["Direct on site", "Direct on site", "Direct on site", "Direct on site", "Ticket/request", "Direct"],
        "Note": ["Very crypto-friendly", "Accepts BTC+USDT", "Accepts crypto", "Accepts crypto", "Ask via ticket", "Free wallet"],
    }))

    st.markdown("---")

    # Gift cards
    st.subheader("🎁 Gift Cards — Buy Any Brand With USDT")
    st.markdown("""
    **Platforms:** Bitrefill, CoinGate, Cryptorefills, Gift-off
    
    Brands available: **Amazon, Apple, Google Play, Steam, PlayStation, Netflix, Uber, Airbnb, Sephora, Best Buy** + 100+ more.
    
    You buy a digital gift card code with USDT → use it like cash on the brand's website.
    """)

    # Meta/Google ads
    st.subheader("🎯 Advertising — Pay for Ads With USDT")
    st.markdown("""
    **The problem:** Meta (Facebook/Instagram) and Google stopped accepting credit cards for high-spend ad accounts as of April 2026.
    
    **The solution:**
    """)
    render_table(pd.DataFrame({
        "Platform": ["Meta Ads via Bleap/RedotPay", "Google Ads via Moon", "Twitter/X Ads", "Reddit Ads", "TikTok Ads"],
        "Method": ["Virtual US BIN card", "Moon virtual card", "Direct via exchange", "Direct via exchange", "Direct via exchange"],
        "Works?": ["✅ Yes", "✅ Yes", "⚠️ Sometimes", "⚠️ Sometimes", "⚠️ Sometimes"],
        "USDT In": ["✅ Direct", "✅ Direct", "⚠️ Requires account", "⚠️ Requires account", "⚠️ Requires account"],
        "Note": ["US BIN critical for Google/Meta", "Moon wallet solution", "Account verification needed", "Varies by region", "Varies by region"],
    }))

    st.markdown("---")

    # Gold
    st.subheader("🥇 Gold & Silver — Physical Delivery")
    render_table(pd.DataFrame({
        "Platform": ["SuisseGold", "Kitco", "Silver Gold Bull", "Kraken (XAUT token)", "Paxos (PAXG token)"],
        "What": ["Physical gold/silver, delivered", "Physical gold, stored or delivered", "Physical gold/silver", "Tokenized gold on-chain", "Tokenized gold on-chain"],
        "USDT": ["✅ Direct", "⚠️ Via exchange", "⚠️ Via exchange", "✅ Direct", "✅ Direct"],
        "Storage": ["Vault or delivery", "Vault or delivery", "Delivery only", "Custodied by Paxos", "Custodied by Paxos"],
    }))

    st.markdown("---")

    # Cards
    st.subheader("💳 The Easy Button — Crypto Debit Cards")
    st.markdown("""
    **Get a crypto card. Spend USDT anywhere Visa/Mastercard is accepted.**
    
    Your USDT converts to USD automatically at point of sale. You spend, it converts.
    """)
    render_table(pd.DataFrame({
        "Card": ["Bleap Mastercard", "RedotPay", "BitPay", "Bybit Card", "Crypto.com"],
        "USDT In": ["✅", "✅", "✅", "✅", "✅"],
        "Cashback": ["2% USDC", "Up to 5%", "1.5%", "Up to 10%", "Up to 5%"],
        "ATM": ["Free to $400/mo", "Low fee", "~$2.50", "Free tiered", "Free tiered"],
        "Best For": ["Media buyers + spenders", "High cashback", "Established", "No stake req.", "CRO stakers"],
        "KYC": ["Minimal", "Minimal", "Yes", "Yes", "Yes"],
    }))

    st.markdown("---")
    st.caption("⚠️ Conversion via card = USD at that moment. Not a capital gains event unless you exchange at a profit. Spending at par = $0 tax.")


def page_limits():
    st.title("📊 Spending Limits — How Much Can You Actually Spend?")
    st.subheader("The real limits on crypto cards, merchants, and payment methods for $10M USDT.")
    st.markdown("---")

    st.success("""
    **The real answer for $10M:** Most individual payment methods cap out at $250K–$1M/day.
    
    **To spend $10M in a month, you need to stack multiple methods.**
    """)

    st.markdown("---")

    st.subheader("💳 Crypto Debit Card Limits")
    render_table(pd.DataFrame({
        "Card": ["RedotPay", "Bleap Mastercard", "Gnosis Pay", "YesCard", "Bitget Card", "Bybit Card", "Crypto.com"],
        "Daily Spend": ["$1,000,000", "$100,000+", "$1,000,000", "$250,000/mo", "$50,000", "$50,000", "$25,000"],
        "Monthly Limit": ["Unlimited", "$400K+", "Unlimited", "$250,000", "$100,000", "$100,000", "$50,000"],
        "ATM/Day": ["$100,000", "$400 free/mo", "Varies", "Varies", "$2,000", "$2,000", "$1,500"],
        "Per Transaction": ["$100,000", "Varies", "$1M", "$100,000+", "$50,000", "$50,000", "$10,000"],
        "KYC": ["Minimal", "Minimal", "None", "Yes", "Yes", "Yes", "Yes"],
        "Best For": ["High spenders", "Daily use", "DeFi users", "Ad buyers", "General", "General", "CRO holders"],
    }))

    st.markdown("---")

    st.subheader("📈 Spend $10M/Month — Stacking Strategy")
    st.markdown("""
    **No single card handles $10M/month.** Here's how to stack:
    """)
    render_table(pd.DataFrame({
        "Method": ["RedotPay card", "Bleap Mastercard", "YesCard (10 cards)", "Direct bank (borrowed USD)", "P2P cash", "Business bank transfer"],
        "Limit": ["$30M/month", "$12M/month", "$2.5M/month", "Unlimited", "Unlimited", "Unlimited"],
        "Daily": ["$1M/day", "$100K/day", "$250K/mo each", "Unlimited", "Unlimited", "Unlimited"],
        "Fees": ["~1%", "~1%", "~1%", "Wire fee", "0.5–2%", "$0–25"],
        "Stack Total": ["$30M+", "$12M+", "$2.5M+", "$10M+", "$5M+", "Unlimited"],
    }))

    st.markdown("---")

    st.subheader("🎯 Ad Spend Limits (Google, Meta, TikTok)")
    render_table(pd.DataFrame({
        "Platform": ["Google Ads", "Meta Ads", "TikTok Ads", "Twitter/X Ads", "Reddit Ads", "LinkedIn Ads"],
        "Via Card": ["Bleap/YesCard (US BIN)", "Bleap/YesCard (US BIN)", "YesCard confirmed", "Varies", "Varies", "Varies"],
        "Daily Limit": ["$1M/day (Bleap)", "$1M/day (Bleap)", "$250K/mo", "$100K+?", "$50K?", "$50K?"],
        "Confirmed Works?": ["✅ Yes", "✅ Yes", "✅ Yes (YesCard)", "⚠️ Sometimes", "⚠️ Sometimes", "⚠️ Sometimes"],
        "Note": ["US BIN critical", "US BIN critical", "$250K/mo confirmed", "Account verify needed", "Account verify needed", "Account verify needed"],
    }))

    st.markdown("---")

    st.subheader("🏠 Big Purchases — Real Estate, Cars, Gold")
    render_table(pd.DataFrame({
        "Purchase": ["Real Estate", "Luxury Cars", "Planes/Yachts", "Gold/Silver", "Business Acquisition"],
        "Min": ["$50K–$500K", "$20K–$100K+", "$100K–$1M+", "$100–$100K+", "$100K–$10M+"],
        "Max": ["Unlimited", "$10M+", "$50M+", "Unlimited (vault)", "Unlimited"],
        "USDT Direct?": ["⚠️ Via escrow/RealOpen", "⚠️ Via intermediary", "⚠️ Direct negotiation", "✅ Via SuisseGold", "⚠️ Negotiate directly"],
        "Tax Event?": ["No (spending)", "No (spending)", "No (spending)", "No (spending)", "No (spending)"],
        "Time": ["Days–weeks", "Days–weeks", "Weeks", "Days", "Weeks–months"],
    }))

    st.markdown("---")

    st.subheader("🌍 Payroll Limits")
    render_table(pd.DataFrame({
        "Platform": ["Bitwage", "Deel", "Remote", "Direct (Gnosis Safe)", "Wise Business"],
        "Per Payment": ["Unlimited", "Unlimited", "Unlimited", "Unlimited", "$1M–$10M"],
        "Per Month": ["Unlimited", "Unlimited", "Unlimited", "Unlimited", "Unlimited"],
        "Per Person": ["Unlimited", "Unlimited", "Unlimited", "Unlimited", "Varies"],
        "Fee": ["0.5–1%", "0% employer", "Custom", "Gas only (<$1)", "~1%"],
        "Note": ["Contractors only", "Full compliance", "Full compliance", "For your own team", "Bank-backed"],
    }))

    st.markdown("---")

    st.subheader("🎁 Gift Card Limits")
    render_table(pd.DataFrame({
        "Platform": ["Bitrefill", "CoinGate", "Cryptorefills", "Binance Gift Cards", "Bitget Gift Cards"],
        "Daily Limit": ["$50,000", "$10,000–50,000", "$10,000–25,000", "$1,000,000", "$50,000"],
        "Per Card": ["$500–$10,000", "$25–$500", "$25–$1,000", "Varies", "$25–5,000"],
        "KYC": ["Email only", "Email only", "Email only", "Exchange account", "Exchange account"],
        "Brands": ["100+", "500+", "200+", "50+", "50+"],
        "Note": ["Hacked in Mar 2026 ⚠️", "Longstanding", "EU focused", "High limit direct", "Growing"],
    }))

    st.markdown("---")

    st.subheader("🏦 IRS / Tax Reporting Thresholds")
    render_table(pd.DataFrame({
        "Rule": [
            "Form 1099-DA from exchanges",
            "1099-MISC (income >$600)",
            "Backup withholding (missing TIN)",
            "FATF Travel Rule (on-chain)",
            "Bank SAR (suspicious activity)",
            "Bank CTR (cash over $10K)",
            "FBAR (foreign accounts >$10K)",
            "FinCEN MSA (money transmitter)",
        ],
        "Threshold": [
            "Any sale/disposal on exchange",
            "$600+ in crypto income",
            "W-9 not provided",
            "$1,000+ on-chain transfer",
            "Anything suspicious",
            "$10,000 cash in one day",
            "$10,000+ in foreign exchanges",
            "Operating as money transmitter",
        ],
        "Who Cares": [
            "Exchanges report to IRS",
            "Platforms report to IRS",
            "Exchange withholds 24%",
            "Data travels with tx",
            "Bank → FinCEN",
            "Bank → FinCEN",
            "Treasury → IRS",
            "Always",
        ],
    }))

    st.markdown("---")

    st.subheader("💡 The $10M/Month Stacking Plan")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **Week 1–4 Spend:**
        | Method | Amount |
        |---|---|
        | Bleap Mastercard | $400K |
        | RedotPay | $4M |
        | P2P cash withdrawals | $2M |
        | Gift cards | $500K |
        | Payroll (Bitwage) | $1M |
        | Real estate escrow | $2M |
        | **Total** | **$9.9M** |
        """)
    with col2:
        st.markdown("""
        **Big Ticket Items:**
        | Item | USDT |
        |---|---|
        | Real estate (via RealOpen) | $3–5M |
        | Vehicle / boat | $500K–2M |
        | Business acquisition | $1–10M |
        | Payroll / contractors | $1–3M/mo |
        | Gold (SuisseGold) | $500K–1M |
        | Ad campaigns | $500K–2M/mo |
        """)
    with col3:
        st.markdown("""
        **Key takeways:**
        - No single method = $10M/month
        - Stack 5–10 methods
        - Cards = $1M/day max combined
        - P2P = unlimited cash
        - Payroll = unlimited USDT out
        - Real estate = single biggest chunk
        """)

    st.markdown("---")
    st.caption("⚠️ Limits change often. Verify with each platform before relying on specific numbers.")


def page_deep_dive():
    st.title("🔍 How the Money Actually Flows")
    st.subheader("Step-by-step: USDT in → cash/spending out. No KYC. No exchanges.")
    st.markdown("---")

    st.success("""
    **For each method:** The exact technical flow — where USDT goes, who touches it, how cash comes out, and where the KYC happens (or doesn't).
    """)

    st.markdown("---")

    # ── Card 1: Bleap ─────────────────────────────────────────────────────────
    st.subheader("💳 Bleap Mastercard — How USDT Becomes Cash")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow:**
        ```
        YOU                               BLEAP                         MERCHANT
        ──────────────────────────────────────────────────────────────────────
        1. Download Bleap app
        2. Connect USDT wallet (self-custody MPC)
        3. Verify identity (minimal KYC — phone + basic info)
        4. Bleap issues virtual Mastercard (instant)
        5. Physical card mailed (3–7 days)

        SPENDING:
        6. You buy something for $500
        7. Bleap converts USDT → USD at current rate (~0.5–1% spread)
        8. Bleap sends USD to merchant via Mastercard network
        9. Merchant receives USD. You receive 2% cashback in USDC.

        ATM WITHDRAWAL:
        10. You withdraw $500 at ATM
        11. Bleap converts USDT → USD
        12. ATM dispenses cash
        13. Fee: ~$2.50 + 1% FX if international
        ```
        """)
        st.markdown("""
        **Where KYC happens:** Minimal — phone number + basic identity. Not on-chain. Bleap knows your name.
        **Where USDT goes:** Bleap holds it in their liquidity pool (custodial). They are the ones converting it.
        **How you get cash:** ATM or spending at any Mastercard merchant.
        **Tax event?** No — spending at par is not a sale. Converting USDT → USD is technically a disposal but at $1.00 = $1.00, so $0 gain.
        **Limitations:** $100K+/day, $400K+/month. Good for daily spend, not for $1M purchases.
        """)

    st.markdown("---")

    # ── Card 2: RedotPay ───────────────────────────────────────────────────────
    st.subheader("💳 RedotPay — How USDT Becomes Cash")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow:**
        ```
        YOU                               REDOTPAY                       WORLD
        ──────────────────────────────────────────────────────────────────────
        1. Download RedotPay app
        2. Top up with USDT (send to RedotPay wallet address)
        3. RedotPay holds USDT in their custodial wallet
        4. Apply for card (virtual instant, physical 5–10 days)
        5. Card linked to your USDT balance

        SPENDING:
        6. You buy $10,000 item
        7. RedotPay debits $10,100 USDT from your balance (includes fee)
        8. RedotPay sends $10,000 USD to merchant via Visa
        9. Merchant receives USD. You pay ~1% fee.

        ATM:
        10. Withdraw $1,000 at ATM
        11. RedotPay debits $1,020 USDT
        12. ATM gives you cash
        13. Fee: ~2% for ATM withdrawals

        CASH-OUT LARGE:
        14. Request large withdrawal via app
        15. RedotPay wires USD to your bank account
        16. Fee: ~1% + wire fee
        17. Time: 1–3 business days
        ```
        """)
        st.markdown("""
        **Where KYC happens:** App signup — phone + ID verification. They have your identity.
        **Where USDT goes:** RedotPay's custodial wallet. They manage the conversion.
        **How you get cash:** ATM (up to $100K/day), bank wire ($1M+/day possible), card spend.
        **Key advantage:** Highest published limits — $1M/day spend, $100K+/mo ATM.
        **Tax event?** Same as Bleap. No capital gains since USDT = $1.00.
        **Note:** If you're sending large amounts into RedotPay, that on-chain transaction is visible on TRON/Ethereum.
        """)

    st.markdown("---")

    # ── Card 3: Gnosis Pay ────────────────────────────────────────────────────
    st.subheader("💳 Gnosis Pay — How USDT Becomes Cash (Self-Custody)")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow:**
        ```
        YOU                               GNOSIS PAY                    WORLD
        ──────────────────────────────────────────────────────────────────────
        1. Have a Gnosis Safe wallet (multisig, self-custody)
        2. Connect Safe to Gnosis Pay
        3. No account creation needed — uses your existing Safe

        FUNDING:
        4. Deposit USDT/USDC into your Safe wallet (any amount)
        5. Gnosis Pay creates a virtual Visa card linked to Safe balance

        SPENDING:
        6. You buy $500 at a store
        7. Gnosis Pay checks: is there enough in the Safe? Yes.
        8. Gnosis Pay authorizes the transaction
        9. Settlement: Gnosis Pay debits your Safe after 3-min delay
        10. Gnosis Pay converts USDT → USD (on their end) and pays merchant
        11. You get up to 4% cashback in USDC

        CANCELLATION WINDOW:
        12. 3-minute window to cancel any transaction from your Safe
        13. After 3 min, Gnosis Pay settles the transaction
        ```
        """)
        st.markdown("""
        **Where KYC happens:** Almost none — Gnosis Pay has no account. Your Safe IS your account. KYC only if you verify with their partner banks.
        **Where USDT goes:** YOUR Safe wallet. Gnosis Pay NEVER holds your funds. They only authorize transactions from your Safe.
        **How you get cash:** Card spend anywhere. ATM via compatible ATMs. Direct wallet → merchant.
        **Key advantage:** Truly non-custodial. No company can freeze your money. Highest daily limit ($1M/day).
        **Limitation:** Must use Gnosis Safe. Newer product, less established. Global ATM network smaller than Bleap/RedotPay.
        **Tax event?** No — you never sold USDT. Gnosis Pay converts it on settlement. You spent from your own wallet.
        """)

    st.markdown("---")

    # ── P2P Binance ───────────────────────────────────────────────────────────
    st.subheader("🤝 Binance P2P — How USDT Becomes Cash (P2P)")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow:**
        ```
        CASH BUYER              YOU (Binance)              USDT SELLER
        ─────────────────────────────────────────────────────────────────
        1. Buyer posts ad: "I'll buy $10K USDT at $1.01 each" (+1% premium)
        2. You accept the trade
        3. Binance HOLDS the seller's $10K USDT in escrow (frozen)
        4. Buyer sends you $10,100 via bank transfer / Zelle / cash
        5. You confirm receipt of cash
        6. Binance RELEASES the $10K USDT to the buyer
        7. You kept the $100 spread as profit

        YOUR CASH IN:
        8. Bank account: +$10,100
        9. Your USDT: unchanged (you weren't the seller)
        ```
        """)
        st.markdown("""
        **Your USDT never moved.** You facilitated the trade. The seller gave USDT, got cash. You took the spread.
        **Where KYC happens:** On Binance — both buyer and seller need Binance account (KYC required by Binance). But YOU don't sell your USDT. You match them.
        **Where USDT goes:** Binance escrow. Never touches you directly.
        **How you get cash:** Buyer pays you via bank transfer, Zelle, PayPal, cash deposit.
        **Tax event?** If YOU are the seller (you sell your USDT): yes, taxable. If you're just matching: you're earning a service fee (ordinary income).
        **Key limit:** Binance P2P fee: 0% taker, 0.15–0.35% maker. Volume: $700M+/day across platform.
        **AML watch:** Binance monitors P2P for fraud. If your counterparty is a scammer, Binance can freeze funds.
        """)

    st.markdown("---")

    # ── Bitwage Payroll ───────────────────────────────────────────────────────
    st.subheader("🌍 Bitwage — How USDT Becomes Payroll")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow:**
        ```
        EMPLOYER                          BITWAGE                        EMPLOYEE
        ──────────────────────────────────────────────────────────────────────
        1. You (employer) fund Bitwage with USDT
        2. Send USDT to Bitwage's wallet address (any amount)
        3. Bitwage holds USDT in their account

        PAYROLL RUN:
        4. You upload payroll (names, amounts, wallet addresses)
        5. Bitwage converts USDT → desired token if needed
        6. Bitwage sends crypto directly to each employee's wallet
        7. Employee receives USDT/USDC in their own wallet
        8. Employee cashes out via their own method (P2P, card, etc.)

        TAX COMPLIANCE:
        9. Bitwage generates 1099 / W-2 for US employees
        10. Bitwage handles W-4, I-9 verification
        11. Employer pays in USDT — Bitwage handles the rest
        ```
        """)
        st.markdown("""
        **Where KYC happens:** Bitwage KYC is on the EMPLOYER and EMPLOYEE side. They verify identities. You (employer) need to register.
        **Where USDT goes:** Bitwage's operational wallet. They pay out from there.
        **How employee gets cash:** Employee chooses — USDT to their own wallet. They off-ramp themselves via their own P2P/card.
        **Tax event?** Employer: USDT paid for salaries = business expense. No capital gains. Employee: income when received.
        **Key advantage:** You never touch the banking system for payroll. USDT in → USDT out → employee handles their own off-ramp.
        **Fees:** 0.5–1% per payroll run. No cost per employee.
        **For $10M:** Pay 100 contractors $100K each. No banks needed.
        """)

    st.markdown("---")

    # ── RealOpen Real Estate ──────────────────────────────────────────────────
    st.subheader("🏠 RealOpen — How USDT Becomes Property")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow:**
        ```
        BUYER                           REALOPEN                      SELLER/ESCROW
        ──────────────────────────────────────────────────────────────────────
        1. Verify crypto holdings (show wallet balance)
        2. Submit offer on property
        3. Lock in USDT → USD conversion rate
        4. Send USDT to RealOpen's deposit address
        5. RealOpen converts USDT → USD (their liquidity partner does this)
        6. RealOpen wires USD to escrow company
        7. Escrow closes like a normal cash sale
        8. Title transfers to you. You own the property.
        ```
        """)
        st.markdown("""
        **Where KYC happens:** Title company / escrow will want ID for the property purchase (standard real estate KYC). RealOpen verifies funds. Not on-chain.
        **Where USDT goes:** RealOpen's wallet. They convert it to USD through a partner (bank or exchange). Wire to escrow.
        **How you get property:** Title in your name. Done through normal escrow process.
        **Tax event?** No — you spent USDT, didn't sell it. RealOpen's conversion is their sale, not yours.
        **Limits:** Property-dependent. Min: $50K. No max. Can buy $10M property with USDT.
        **Best for:** LATAM, Caribbean, Middle East, Southeast Asia. Growing in US/Europe.
        **Time:** 1–4 weeks for closing.
        """)

    st.markdown("---")

    # ── SuisseGold ────────────────────────────────────────────────────────────
    st.subheader("🥇 SuisseGold — How USDT Becomes Gold")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow:**
        ```
        BUYER                          SUISSEGOLD                    VAULT/DELIVERY
        ──────────────────────────────────────────────────────────────────────
        1. Go to SuisseGold.com, select gold/silver
        2. Choose USDT at checkout
        3. Enter your USDT wallet address (TRC20 or ERC20)
        4. Send exact USDT amount to provided address
        5. Wait for blockchain confirmation (TRON: ~3 min, ETH: ~15 min)
        6. SuisseGold receives USDT, confirms payment
        7a. OPTION A: Gold stored in Swiss vault (cheaper, no delivery)
        7b. OPTION B: Physical delivery to your address (armored courier)
        ```
        """)
        st.markdown("""
        **Where KYC happens:** SuisseGold may require ID for large purchases (>10kg). For smaller amounts: minimal verification.
        **Where USDT goes:** SuisseGold's wallet. They receive USDT directly. Gold stays in Swiss vault.
        **How you get value:** (A) Vault storage — you own it, can sell back to SuisseGold. (B) Physical delivery — armored courier to your door.
        **Tax event?** Buying gold with USDT = no capital gains. Selling gold back = capital gains. Storage fee: ~0.1%/yr.
        **Tokenized alternative:** XAUT (Tether Gold) — tokenized gold on Kraken. USDT → XAUT directly. No physical delivery.
        """)

    st.markdown("---")

    # ── Gift Cards ────────────────────────────────────────────────────────────
    st.subheader("🎁 Gift Cards — How USDT Becomes Any Brand")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow (Bitrefill/CoinGate):**
        ```
        BUYER                           PLATFORM                       BRAND
        ──────────────────────────────────────────────────────────────────────
        1. Select gift card (Amazon, Apple, Steam, etc.)
        2. Choose amount (e.g., $500 Amazon)
        3. Select USDT as payment
        4. Send exact USDT to platform's wallet address
        5. Wait for 1–6 blockchain confirmations
        6. Platform confirms payment
        7. Gift card code delivered instantly (email / dashboard)
        8. Redeem on brand's website as cash equivalent
        ```
        """)
        st.markdown("""
        **Where KYC happens:** Bitrefill / CoinGate — email only for small amounts. No ID needed up to limits.
        **Where USDT goes:** Platform's wallet. You send USDT, they send code.
        **How you use it:** Enter code on Amazon/Apple/etc. It works like cash.
        **Tax event?** No — buying a gift card is spending, not investing. No capital gains.
        **Limits:** Bitrefill: up to $50K/day per transaction. CoinGate: $10K–50K/day.
        **⚠️ Bitrefill was HACKED March 2026:** Compromised employee laptop. 18,500 records exposed. Platform offline temporarily. Use CoinGate as alternative.
        """)

    st.markdown("---")

    # ── Ad Spend ──────────────────────────────────────────────────────────────
    st.subheader("🎯 Ad Spend (Meta/Google) — How USDT Becomes Ad Spend")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow (Bleap/RedotPay → Meta/Google):**
        ```
        YOU                              CARD                          PLATFORM
        ──────────────────────────────────────────────────────────────────────
        1. Get Bleap or RedotPay card with US Visa BIN
        2. Add card as payment method in Meta Business Manager
        3. Google Ads account: add card as payment method
        4. Run ads — charges hit your card
        5. Bleap converts USDT → USD at point of charge
        6. Meta/Google receives USD. Your ads run.
        7. Monthly bill: charged to your card automatically
        ```
        """)
        st.markdown("""
        **Why US BIN matters:** Meta/Google flag or reject cards from non-US/EU BINs. US Visa = accepted. TRC20 USDT BIN = flagged.
        **The key:** Cards with US Visa BINs (YesCard, Bleap, RedotPay) work directly on Meta and Google.
        **YesCard specifically:** Confirmed to work on Meta, Google, TikTok, Snapchat. $250K/month limit.
        **Tax event?** No — spending on ads is a business expense. USDT → Mastercard network → USD. Not a taxable event.
        **Key limits:** Meta/Google charge at month's end. Large ad budgets = large card charges. Stack multiple cards for >$250K/mo ad spend.
        """)

    st.markdown("---")

    # ── Travala Travel ───────────────────────────────────────────────────────
    st.subheader("✈️ Travala — How USDT Becomes Travel")
    with st.expander("Step-by-step flow"):
        st.markdown("""
        **The flow:**
        ```
        BUYER                            TRAVALA                      HOTEL/AIRLINE
        ──────────────────────────────────────────────────────────────────────
        1. Select hotel or flight on Travala.com
        2. Choose USDT at checkout
        3. Travala shows wallet address (or QR code)
        4. Send exact USDT amount to Travala's wallet
        5. Travala confirms on-chain (1–3 confirmations)
        6. Travala converts USDT → fiat (behind the scenes)
        7. Travala pays hotel/airline via their bank account
        8. Booking confirmed. You receive confirmation email.
        ```
        """)
        st.markdown("""
        **Where KYC happens:** Travala may ask for ID if booking >$3,000 or if suspicious. Hotel may ask for ID at check-in.
        **Where USDT goes:** Travala's wallet. They handle the conversion to fiat for the merchant.
        **How you travel:** Booking confirmation is all you need. Hotel gets paid by Travala. You show up, check in.
        **Tax event?** No — buying travel with USDT is spending, not selling.
        **Catalog:** 2M+ hotels, 600+ airlines, cars, experiences in 230+ countries.
        **Alternatives:** PayBito, Cryptovago, Cheapie — similar flows.
        """)

    st.markdown("---")

    # ── The Big Picture ──────────────────────────────────────────────────────
    st.subheader("💡 The Pattern — Every Method Has the Same Structure")
    st.markdown("""
    **Every USDT → Cash/Spending method follows this pattern:**
    ```
    YOU ($10M USDT in wallet)
         ↓
    SEND USDT to a company / platform / escrow
    (on-chain transaction — visible on blockchain)
         ↓
    PLATFORM holds or converts USDT
         ↓
    PLATFORM sends USD / service / goods to the recipient
    (merchant, seller, employee, yourself via ATM)
         ↓
    YOU get what you bought
    (cash, property, goods, services, travel)
    ```
    
    **The conversion always happens on THEIR side, not yours.**
    
    | Method | Who Converts? | Where Your USDT Goes |
    |---|---|---|
    | Crypto card | Bleap/RedotPay | Their liquidity pool |
    | Gnosis Pay | Nobody (self-custody) | Your own Safe |
    | P2P | Binance escrow | Not yours |
    | Bitwage | Bitwage | Their wallet → employee |
    | RealOpen | RealOpen partner | Their wallet → escrow |
    | SuisseGold | SuisseGold | Their wallet → vault |
    | Gift cards | Bitrefill/CoinGate | Their wallet → code |
    | Ad spend | Bleap/YesCard | Their pool → Mastercard |
    | Travel | Travala | Their wallet → hotel/airline |
    """)

    st.markdown("---")
    st.caption("⚠️ Every on-chain transaction from your wallet is visible on the blockchain. Use fresh wallet addresses for large transfers.")


def page_requirements():
    st.title("📋 Signup Requirements — What You Need for Each")
    st.subheader("KYC level, documents, time, and costs to get each method working.")
    st.markdown("---")

    st.success("""
    **TL;DR:**
    - **Easiest:** Gift cards (Bitrefill/CoinGate) — email only, instant
    - **Fastest:** Crypto cards (Bleap/RedotPay) — phone + ID, minutes
    - **Most private:** Gnosis Pay — no account, just a Safe wallet
    - **Heaviest KYC:** RealOpen, SuisseGold (>CHF 10K), Bitwage employers
    - **Binance P2P:** Full government ID + selfie required
    """)

    st.markdown("---")

    render_table(pd.DataFrame({
        "Method": [
            "Bleap Mastercard", "RedotPay", "Gnosis Pay", "Binance P2P",
            "Bitwage", "RealOpen", "SuisseGold (<CHF 10K)", "SuisseGold (>CHF 10K)",
            "Bitrefill", "CoinGate", "YesCard", "Travala",
        ],
        "KYC Level": [
            "Medium", "Medium", "Minimal", "Heavy",
            "Medium", "Heavy", "Light", "Heavy",
            "None (email)", "None (email)", "Medium", "Light",
        ],
        "Documents Needed": [
            "Gov ID + selfie + proof of address", "Gov ID + selfie + phone", "Just a Safe wallet", "Passport/ID + selfie + proof of address",
            "Business docs + EIN + admin ID", "Gov ID + proof of funds + property docs", "Name + email + address", "Gov ID + proof of address + source of funds",
            "Email only", "Email only", "Gov ID + selfie", "Account (KYC for large bookings)",
        ],
        "Time to Active": [
            "Minutes–hours", "Minutes–hours", "Instant (if you have Safe)", "Hours–days",
            "Days–1 week", "Weeks (property closing)", "Minutes", "Hours–days",
            "Instant", "Instant", "Hours–days", "Instant (email)",
        ],
        "Cost": [
            "$0 (free card)", "$0 (free card)", "$0 (free)", "$0",
            "0.5–1% per run", "0.5–2% on purchase", "1–3% premium", "1–3% + ID admin",
            "1–5% per card", "1–5% per card", "$0 (3% top-up fee)", "0–2%",
        ],
        "Best For": [
            "Daily spenders", "High volume spenders", "Privacy-first users", "Matching P2P trades",
            "International payroll", "Property purchases", "Small gold buys", "Large gold purchases",
            "Gift card arbitrage", "Gift cards (post-Bitrefill hack)", "Ad buyers", "Travel bookings",
        ],
    }))

    st.markdown("---")

    # Detailed breakdowns
    st.subheader("💳 Bleap Mastercard — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **Basic Verification (starts here):**
        - Government-issued ID (passport, driver's license, national ID)
        - Clear selfie (for face matching)
        - Phone number
        - Email address

        **Higher Verification (unlocks higher limits):**
        - All of the above PLUS:
        - Proof of address (utility bill, bank statement, or government letter)
        - Must be issued in last 3 months
        - Must match your registered name and address

        **Time:** Minutes for basic, hours for higher verification
        **Cost:** $0 — card is free, no monthly fee, no FX fee
        **Limits after verification:**
        - Basic: ~$5K/month
        - Higher: $100K+/day, $400K+/month
        """)

    st.markdown("---")

    st.subheader("💳 RedotPay — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **Signup:**
        - Email address
        - Phone number
        - Government-issued ID (passport, driver's license)
        - Biometric verification (in-app selfie/camera)

        **How KYC works:**
        - RedotPay uses automated KYC (AML checks against global databases)
        - Typically completes within minutes
        - May require manual review for large amounts or suspicious activity

        **Time:** Minutes to hours
        **Cost:** $0 to sign up. 3% top-up fee if loading with card. 1% FX. 2% ATM.
        **Limits after verification:** $1M/day spend, $100K+/month ATM
        """)

    st.markdown("---")

    st.subheader("💳 Gnosis Pay — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **The unique thing about Gnosis Pay:** It uses your existing Gnosis Safe wallet. There's no account to create.

        **Requirements:**
        - A Gnosis Safe wallet (multi-sig, set up in minutes at safe.global)
        - EURe stablecoin in your Safe (or USDT/USDC via conversion)
        - For European users — the physical card may require additional KYC from their banking partner

        **What you DON'T need:**
        - No government ID
        - No selfie
        - No proof of address
        - No phone number
        - No account with Gnosis Pay specifically

        **How it works technically:**
        - Gnosis Pay creates a virtual Visa card linked to your Safe
        - Your Safe IS your account
        - No middleman holds your funds
        - 3-minute cancellation window on all transactions

        **Limitations:**
        - Must have a Gnosis Safe already (takes 5 min to set up)
        - Available primarily in EU/EEA (as of 2026)
        - Uses EURe (Euro stablecoin) by default, not USDT/USDC
        - Higher limits available with partner bank KYC

        **Cost:** $0 — no fee to set up Safe, no fee for Gnosis Pay
        """)

    st.markdown("---")

    st.subheader("🤝 Binance P2P — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **Binance requires full KYC to use P2P at all in 2026.**

        **Level 1 (minimum for P2P):**
        - Full name
        - Date of birth
        - Country of residence
        - Government-issued ID (passport, driver's license, national ID)
        - Face verification (selfie/video)

        **Level 2 (higher limits, unlocks all features):**
        - All of Level 1 PLUS
        - Proof of address (utility bill or bank statement < 3 months)
        - May require additional verification

        **Business accounts:**
        - Company registration documents
        - Company bank account verification
        - Director ID verification

        **How P2P works differently:**
        - As a P2P MATCHER (not a seller): You need a Binance account to post ads. Full KYC required.
        - As a CASH BUYER: You need to pay the USDT seller. KYC is on the seller.
        - Binance holds USDT in escrow. Both parties' IDs are on file with Binance.

        **⚠️ The problem for privacy:** Binance reports to governments. Your ID is on file with Binance for every P2P trade.

        **Time:** Hours to days
        **Cost:** $0 to sign up, 0% taker fee, 0.15–0.35% maker fee for posting ads
        """)

    st.markdown("---")

    st.subheader("🌍 Bitwage — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **Employer signup (you paying others):**
        - Business name and entity type
        - EIN / Tax ID
        - Admin contact info (name, email, phone)
        - Business address
        - Bank account or USDT funding source
        - For US employees: W-4 forms required
        - For contractors: 1099 generation provided by Bitwage

        **Contractor/employee signup:**
        - Name and email
        - Wallet address for crypto payout (they control the wallet)
        - For US workers: W-4 or W-9 form
        - For international: varies by country

        **How it works:**
        - You fund Bitwage with USDT (any amount)
        - Bitwage converts and distributes to employees
        - Employees choose to receive as USDT, USDC, or local fiat

        **KYC is on the employees, not you:**
        - You (employer) verify your business
        - Each employee verifies their identity to Bitwage
        - You never see their banking info

        **Time:** Days to set up employer account. Employees can sign up instantly.
        **Cost:** 0.5–1% per payroll run. No cost per employee.
        """)

    st.markdown("---")

    st.subheader("🏠 RealOpen — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **To use RealOpen for USDT real estate purchases:**

        **Identity verification:**
        - Government-issued photo ID (passport preferred)
        - Selfie for face matching
        - Proof of address (utility bill, bank statement < 3 months)
        - Source of funds documentation (showing where the USDT came from)

        **Property requirements:**
        - Minimum purchase: typically $50K–$500K depending on property/location
        - Must be using USDT (or other accepted crypto)
        - Property must be verified by RealOpen

        **Process:**
        1. Verify identity with RealOpen
        2. Show proof of USDT holdings (wallet screenshot)
        3. Lock in USDT/USD conversion rate
        4. Send USDT to RealOpen deposit address
        5. RealOpen converts → wires to escrow
        6. Title company closes the deal

        **The escrow/title company ALSO wants KYC:**
        - Standard real estate KYC applies
        - This is separate from RealOpen's KYC
        - ID, proof of funds, etc.

        **Time:** 1–4 weeks for property closing
        **Cost:** 0.5–2% on the transaction
        """)

    st.markdown("---")

    st.subheader("🥇 SuisseGold — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **Under CHF 10,000 (~$11,000):**
        - Name
        - Email
        - Wallet address (TRC20 or ERC20)
        - No ID required
        - Instant purchase

        **CHF 10,000–100,000:**
        - Government-issued ID
        - Proof of address
        - AML form completed
        - Source of funds (declaration)

        **Over CHF 100,000:**
        - All of the above PLUS
        - Enhanced due diligence
        - May require in-person verification
        - Enhanced source of funds documentation

        **Gold delivery (if physical):**
        - Delivery address
        - May require signature on delivery
        - Armored delivery for large amounts

        **Switzerland-specific:**
        - No purchase license required for foreign buyers
        - Swiss AML law applies (FINMA regulations)
        - All transactions recorded per Swiss law

        **Time:** Instant for small amounts. Hours to days for larger purchases.
        **Cost:** 1–3% premium over spot gold price. Vault storage: ~0.1%/yr.
        """)

    st.markdown("---")

    st.subheader("🎁 Gift Cards — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **Bitrefill (post-hack March 2026):**
        - Email only for purchases under ~$500
        - For higher limits: government ID may be required
        - Account creation free
        - ⚠️ Hack in March 2026 — 18,500 records exposed. Use with caution.
        - Catalog: 3,000+ brands, instant delivery

        **CoinGate (recommended alternative to Bitrefill):**
        - Email only for basic purchases
        - Higher limits with account verification
        - No government ID required for most purchases
        - 500+ brands, instant digital delivery
        - Strong alternative post-Bitrefill breach

        **Binance Gift Cards:**
        - Requires Binance account (full KYC)
        - Gift cards up to $1M/day
        - No recipient KYC needed

        **Bitget Gift Cards:**
        - Requires Bitget account (KYC)
        - $25–$5,000 per card range
        - Instant delivery

        **Key insight:** For gift cards, you CAN stay nearly anonymous if you keep purchases small (<$500). The platform has your email, not your government ID.
        """)

    st.markdown("---")

    st.subheader("✈️ Travala — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **Basic booking (under $3,000):**
        - Email address
        - Account creation (name + email only)
        - No ID required for booking
        - USDT directly accepted

        **Large bookings (over $3,000):**
        - May require additional verification
        - AML compliance check for large crypto transactions
        - Travala can refuse or freeze if compliance fails

        **Hotel check-in:**
        - Hotel will ask for ID at check-in (standard hotel practice)
        - Not Travala's requirement — the hotel's

        **Payment options:**
        - USDT direct (TRC20 recommended — lowest fees)
        - USDC also accepted
        - BTC, ETH, and other coins accepted

        **Time:** Instant booking confirmation. USDT confirmation: 1–3 blockchain confirmations.
        **Cost:** 0% fee for USDT payments (platform discount vs credit card).
        """)

    st.markdown("---")

    st.subheader("🎯 YesCard — Detailed Requirements")
    with st.expander("See full requirements"):
        st.markdown("""
        **Signup process:**
        - Government-issued ID (passport, driver's license)
        - Selfie verification
        - Link crypto wallet (to fund the card)
        - Some tiers may require staking of the platform's token

        **Why it's different from Bleap/RedotPay:**
        - YesCard is specifically designed for media buyers (Meta/Google/TikTok ads)
        - US Visa BIN — confirmed working on major ad platforms
        - Multi-card support — create up to 50 cards
        - Each card can have its own limit

        **Time:** Hours to days for verification
        **Cost:** $0 to create cards. 3% top-up fee.
        **Limits:** $250K/month per card. Up to 50 cards = $12.5M/month.
        """)

    st.markdown("---")

    st.subheader("💡 Best Combo for $10M — Minimal KYC Stack")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Minimal KYC Stack (keep it quiet):**

        | Method | KYC | Limit | Use Case |
        |---|---|---|---|
        | CoinGate | Email only | $50K/day | Gift cards, brand purchases |
        | Gnosis Pay | None | $1M/day | Daily spend, if EU |
        | Bleap (basic) | ID + selfie | $5K/month | Small daily purchases |
        | Bitwage | Employer only | Unlimited | Payroll (employee KYC is on them) |
        | Travala | Email | Travel | Flights + hotels |
        | SuisseGold <10K | Name + email | $11K | Small gold |

        **Total KYC exposure:** Your email + ID on 2 platforms max.
        """)
    with col2:
        st.markdown("""
        **Full Power Stack (unlock $10M/month):**

        | Method | KYC | Limit | Use Case |
        |---|---|---|---|
        | Bleap (higher) | ID + address proof | $400K/mo | Daily operations |
        | RedotPay | Full ID + biometric | $30M/mo | High-volume spend |
        | YesCard (50 cards) | Full ID | $12.5M/mo | Ad spend |
        | RealOpen | Full + property | Unlimited | Real estate |
        | Bitwage | Business EIN | Unlimited | Global payroll |
        | SuisseGold >10K | Full + source of funds | Unlimited | Gold/wealth |

        **Total KYC exposure:** ID + address + business docs on 6+ platforms.
        """)


# ─── App Shell ─────────────────────────────────────────────────────────────────
PAGES = {
    "🏠 Home": page_home,
    "🤝 P2P — Sell USDT for Cash": page_p2p,
    "💳 Borrow Against USDT": page_loans,
    "🏪 Run a USDT Business": page_usdt_biz,
    "🛒 What to Buy With USDT": page_spend,
    "📊 Spending Limits": page_limits,
    "🔍 How Money Flows": page_deep_dive,
    "📋 Signup Requirements": page_requirements,
    "⚠️ Fraud Cases ($10M)": page_fraud,
}

st.sidebar.title("💸 USDT Cash-Out Guide")
st.sidebar.caption("No KYC exchange. Max spending power.")

selection = st.sidebar.radio("Navigate", list(PAGES.keys()), label_visibility="collapsed")
PAGES[selection]()