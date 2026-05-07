import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="USDT → Cash",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

def render(df):
    st.dataframe(df, use_container_width=True, hide_index=True)


def render(df):
    st.dataframe(df, use_container_width=True, hide_index=True)

# ─── PAGE 1: HOME ────────────────────────────────────────────────────────────────
def page_home():
    st.title("💸 USDT → Cash")
    st.subheader("How to turn USDT into cash without government ID. Privacy ranked.")
    st.markdown("---")

    st.success("""
**The goal:** $10M in USDT. Get it out as cash. No government ID. No one seeing it.

**The model:** Two angles — (1) P2P gambling business and (2) put up USDT as collateral, get a loan, bank sees debt not income.
""")

    st.markdown("---")

    st.subheader("All Ways to Get USDT → Cash")

    render(pd.DataFrame({
        "Method": [
            "🤝 P2P — Gamblers buy crypto",
            "💳 Loan — Put up USDT as collateral",
            "🔐 Gnosis Safe — Spend directly",
            "🎁 Gift Cards — Buy, resell for cash",
            "✈️ Flights/Hotels — Buy, resell",
            "💱 DEX — Swap to BTC, sell P2P",
            "👤 Local P2P — In person cash",
            "💳 Debit Cards — Load and spend",
        ],
        "Privacy": [
            "🔴 Low (on platform)",
            "🟡 Medium (they have ID)",
            "🟢 High (no one holds it)",
            "🟢 High (email only)",
            "🟢 High (no ID < $3K)",
            "🟢 High (no ID)",
            "🟢 Highest (cash)",
            "🔴 Low (ID required)",
        ],
        "ID Needed": [
            "None",
            "Yes (for the loan)",
            "None",
            "Email only",
            "No (under $3K)",
            "None",
            "None",
            "ID + selfie",
        ],
        "Best For": [
            "Main business — gamblers",
            "Large amounts to bank",
            "Most private spending",
            "Resell to gamblers",
            "Resell to gamblers",
            "Privacy first",
            "Small amounts, trust",
            "Backup",
        ],
    }))

    st.markdown("---")

    st.subheader("The Privacy Stack")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Most Private", "Local P2P", "Cash in hand")
    col2.metric("Best Tech", "Gnosis Safe", "No one holds it")
    col3.metric("Business", "P2P Gamblers", "Main income")
    col4.metric("Bank Cash", "Loan", "Debt not income")

# ─── PAGE 2: P2P GAMBLERS ────────────────────────────────────────────────────
def page_p2p():
    st.title("🤝 P2P — Gamblers Want to Buy Crypto")
    st.subheader("The main business. Match gamblers to cash. Take the spread.")
    st.markdown("---")

    st.success("""
**The model:**
- Gamblers need USDT to bet on betting sites
- You match them with people who have USDT
- Cash goes to the seller. USDT goes to the gambler. You take a %.

**No government ID. No bank account needed on your end. Just a wallet and Telegram.**
""")

    st.markdown("---")

    st.subheader("How It Works")

    st.markdown("""
```
GAMBLER (has cash)
     ↓
Wants USDT to bet with
     ↓
YOU match them with a USDT SELLER
     ↓
Seller sends USDT to gambler's wallet
     ↓
Gambler pays cash to seller
     ↓
You take 2-5% of every trade
```

**Your USDT never moves.** You're just matching people.
""")

    st.markdown("---")

    st.subheader("Where to Find Gamblers")

    render(pd.DataFrame({
        "Place": ["Telegram P2P groups", "LocalCoinSwap.com", "NoOnes.com", "Your own platform", "LocalBitcoin meetups", "Craigslist / FB Marketplace"],
        "What": ["Crypto trading signal groups, gambling groups", "Decentralized P2P, escrow built-in", "Decentralized P2P, Telegram integration", "Build your own app/website", "In-person cash meets", "Local cash sellers"],
        "Privacy": ["Medium", "High", "High", "You decide", "Highest", "Highest"],
        "Scale": ["Medium", "High", "High", "Unlimited", "Small", "Small"],
        "Your ID": ["None", "None", "None", "None", "None", "None"],
    }))

    st.markdown("---")

    st.subheader("How to Start — Step by Step")

    steps = [
        ("1", "Get a wallet", "Download Trust Wallet or MetaMask. Set it up in 5 minutes."),
        ("2", "Join Telegram groups", "Search: 'crypto P2P', 'USDt buy', 'betting crypto'. Join gambling communities."),
        ("3", "Post an ad", "Say: 'Buying USDT, paying cash, 2% below market'"),
        ("4", "Match buyer and seller", "Connect gambler to USDT holder. Hold USDT in escrow."),
        ("5", "Confirm cash receipt", "Once cash lands, release the USDT."),
        ("6", "Keep the spread", "You made 2-5% on the trade. Repeat."),
    ]

    for num, title, desc in steps:
        col1, col2 = st.columns([1, 5])
        col1.markdown(f"**{num}**")
        col2.markdown(f"**{title}** — {desc}")

    st.markdown("---")

    st.subheader("What Gamblers Want")

    render(pd.DataFrame({
        "What": ["USDT", "Steam Cards", "Amazon Cards", "Apple Cards", "Google Play", "Skrill / Neteller", "Flight/Hotel bookings"],
        "Why": ["For betting sites directly", "Skin gambling sites", "Sell for cash on marketplaces", "Buy apps / sell for cash", "Buy apps / sell for cash", "Direct deposit to betting accounts", "Resell for cash at discount"],
        "Spread You Can Take": ["2-5%", "10-20%", "10-15%", "10-15%", "10-15%", "5-10%", "10-20%"],
    }))

    st.markdown("---")

    st.subheader("Scaling Up — Build Your Own Platform")

    st.markdown("""
**Start:** Telegram + wallet = $0 to start
**Scale:** Build a P2P website or app

**What a platform does:**
- Escrow built in
- User verification (optional — you decide)
- Payment rails (bank transfers, cash meets)
- Dispute resolution
- Volume tracking

**Technology options:**
- White-label P2P software
- Build on NoOnes / LocalCoinSwap API
- Build from scratch

**No ID needed** on your platform if you keep it small.
At scale: FinCEN MSB + basic KYC.
""")

    st.markdown("---")

    st.warning("Paxful warning: Platform shut down Dec 2025. $7.5M fine. No MTL licenses. No AML program.\n\nIf you build a platform: get FinCEN MSB registration ($500/month) + Wyoming MTL before doing serious volume.")

# ─── PAGE 3: LOANS ─────────────────────────────────────────────────────────────
def page_loans():
    st.title("💳 Loan — Put Up USDT, Get Cash")
    st.subheader("Bank sees: personal loan. IRS sees: debt. Not income.")
    st.markdown("---")

    st.success("""
**The key insight:** When you take a loan against your USDT — it's DEBT, not income.

The bank sees: "Personal loan from Ledn Capital"
The IRS sees: "Debt"
You see: Cash in your bank account

**No capital gains. No income tax. Banks don't ask about your collateral.**
""")

    st.markdown("---")

    st.subheader("What the Bank Actually Sees")

    st.markdown("""
```
Wire transfer: $5,000,000
Source: Personal loan — Ledn Capital
Description: Secured personal loan

Monthly payment: $X
Account: Your checking account

THAT'S IT.
```

Banks do NOT see:
- Your USDT wallet
- How much USDT you have
- Where the collateral is
- That it's crypto-backed
""")

    st.markdown("---")

    st.subheader("What Banks Look At")

    render(pd.DataFrame({
        "Bank Checks": ["Your income / credit score", "Debt-to-income ratio", "Payment history", "Monthly payment amount"],
        "Bank Does NOT Check": ["What the loan is collateralized by", "Your crypto holdings", "Where the collateral came from", "Your wallet addresses"],
    }))

    st.markdown("---")

    st.subheader("The Platforms")

    render(pd.DataFrame({
        "Platform": ["Ledn", "Unchained Capital", "Lava Finance", "Aave V3 (DeFi)", "CoinRabbit"],
        "Collateral": ["BTC / ETH", "BTC / ETH", "BTC", "ETH / wstETH", "Multi-asset"],
        "LTV": ["50%", "50%", "50%", "75%", "50%"],
        "APR": ["9.99-11.49%", "12-15%", "~5%", "5-8%", "8-16%"],
        "Output": ["USD wire", "USD wire", "USD wire", "USDC (on-chain)", "USD wire"],
        "ID Required": ["Yes", "Yes", "Some", "No (DeFi)", "Yes"],
        "Best For": ["BTC holders", "BTC holders", "BTC holders", "ETH holders", "Multi-asset"],
    }))

    st.markdown("---")

    st.subheader("The USDT Problem")

    st.markdown("""
Most platforms want **BTC or ETH** as collateral, not USDT.

**Option 1: Swap USDT → BTC/ETH first**
- One taxable event (you're selling USDT)
- Pay the small tax once
- Then take the loan against BTC

**Option 2: Find a platform that takes USDT**
- Aave V3 has USDT pools
- Less common, higher rates

**Option 3: Don't swap — just use the other methods**
- P2P, gift cards, Gnosis Safe spending
- No swap needed
- No tax event
""")

    st.markdown("---")

    st.subheader("Red Flags — Will They Ask Questions?")

    render(pd.DataFrame({
        "Concern": [
            "Is it income?",
            "Do they report to IRS?",
            "Will they ask about crypto?",
            "Do they check wallets?",
            "Does it affect my credit?",
            "What if I don't pay back?",
        ],
        "Answer": [
            "No — it's debt",
            "No — loans aren't reported to IRS",
            "No — they see a loan agreement only",
            "No — collateral is not shown to the bank",
            "Yes — it's debt, shows on credit report",
            "They keep the collateral (like a house foreclosure)",
        ],
    }))

    st.markdown("---")

    st.error("⚠️ **One swap = one taxable event.** If you swap USDT → BTC to get a loan: you sold USDT. Pay the tax on that one sale. Done. Everything after = no tax.")

# ─── PAGE 4: GNOSIS SAFE ────────────────────────────────────────────────────
def page_safe():
    st.title("🔐 Gnosis Safe — Most Private")
    st.subheader("Your wallet. Your USDT. No company holds it. No one can freeze it.")
    st.markdown("---")

    st.success("""
**The key:** Your USDT never leaves your wallet.

Unlike Bleap or RedotPay where the company holds your USDT and converts it — with Gnosis Safe, you spend directly from your own wallet.

No company = no one to freeze your money = most private.
""")

    st.markdown("---")

    st.subheader("What Happens")

    st.markdown("""
```
YOUR GNOSIS SAFE WALLET ($10M USDT)
        ↓
Gnosis Pay creates a virtual Visa card linked to your wallet
        ↓
You buy something for $500
        ↓
Gnosis Pay checks: is there enough in the Safe? Yes.
        ↓
3-minute window to cancel the transaction
        ↓
Transaction settles from YOUR wallet
        ↓
Merchant gets USD
YOU NEVER SOLD ANYTHING
```
""")

    st.markdown("---")

    st.subheader("What You Can Do")

    render(pd.DataFrame({
        "What": ["Online shopping (Amazon, anything)", "In-store NFC tap to pay", "ATM withdrawals", "Bank transfer to another account", "Pay contractors / freelancers", "No 1099 issued to you", "No company can freeze your money"],
        "How": ["Visa accepted anywhere", "Apple Pay / Google Pay", "Compatible ATMs worldwide", "Send from your wallet", "Send USDT directly to their wallet", "It's your wallet, not theirs", "True self-custody"],
    }))

    st.markdown("---")

    st.subheader("vs Other Cards")

    render(pd.DataFrame({
        "Feature": ["Who holds your USDT?", "Can they freeze it?", "Do they have your ID?", "IRS reporting to you?", "Best for"],
        "Bleap": ["Bleap company", "Yes", "Yes (ID + selfie)", "Yes (1099)", "Easy spending"],
        "RedotPay": ["RedotPay company", "Yes", "Yes (ID + selfie)", "Yes", "High limits"],
        "Gnosis Safe": ["YOU", "No — impossible", "No", "No", "Privacy first"],
    }))

    st.markdown("---")

    st.subheader("How to Set Up")

    steps = [
        ("1", "Download Gnosis Safe app", "safe.global or app store"),
        ("2", "Create a wallet", "Write down your seed phrase. Store it somewhere safe."),
        ("3", "Fund it with USDT", "Transfer USDT from wherever you have it"),
        ("4", "Connect to Gnosis Pay", "Inside the app, link your wallet to Gnosis Pay"),
        ("5", "Get a virtual card", "Instant — works right away"),
        ("6", "Start spending", "Tap to pay, online shopping, ATM"),
    ]

    for num, title, desc in steps:
        col1, col2 = st.columns([1, 5])
        col1.markdown(f"**{num}**")
        col2.markdown(f"**{title}** — {desc}")

    st.markdown("---")

    st.warning("⚠️ **Limitation:** Mostly EU/EEA right now. US rollout coming. Check if it works in your country.")

# ─── PAGE 5: GIFT CARDS ──────────────────────────────────────────────────────
def page_gift():
    st.title("🎁 Gift Cards + Flights → Resell for Cash")
    st.subheader("Buy with USDT. Sell to gamblers at a discount. Cash in your pocket.")
    st.markdown("---")

    st.success("""
**The model:**
1. Buy gift cards with USDT (no ID needed)
2. Sell them to gamblers at 10-20% below face value
3. Cash in your pocket

**Gamblers love gift cards** because they use them on betting sites or sell them for cash.
""")

    st.markdown("---")

    st.subheader("CoinGate — Email Only, No ID")

    st.markdown("""
**CoinGate.com:**
- Create account: email only
- Buy: Amazon, Apple, Steam, PlayStation, Google Play, Netflix, Uber, Airbnb + 500+ more
- Pay with: USDT directly
- Delivery: instant code

**No government ID. No selfie. No SSN. Just an email.**
""")

    st.markdown("---")

    st.subheader("What Gamblers Pay Premium For")

    render(pd.DataFrame({
        "Gift Card": ["Steam Cards", "Amazon Cards", "Apple Cards", "Google Play", "PlayStation", "Netflix", "Uber / Lyft", "Airbnb"],
        "Why They Want It": ["Skin gambling sites accept Steam", "Sell for cash / buy things", "Apps, subscriptions", "Apps / sell for cash", "Gaming purchases", "Subscriptions / sell", "Rides / sell for cash", "Travel / sell for cash"],
        "Discount They Pay": ["10-20% below face", "10-15%", "10-15%", "10-15%", "10-15%", "5-10%", "10-15%", "10-15%"],
        "How to Sell": ["Telegram groups", "CardTrader.com", "Reddit r/gcmarket", "Telegram", "Reddit", "Reddit", "Local cash", "Local cash"],
    }))

    st.markdown("---")

    st.subheader("The Math")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Example: Steam Cards**

        1. Buy $1,000 Steam card on CoinGate for $1,000 USDT
        2. Sell to gambler for $850 cash (15% below face)
        3. Profit: $150
        4. Gambler got $1K in gambling credits for $850

        **Win-win.**
        """)
    with col2:
        st.markdown("""
        **Example: Amazon Cards**

        1. Buy $500 Amazon card for $500 USDT
        2. Sell to gambler for $430 cash (14% below)
        3. Profit: $70
        4. Scale: 10 cards/day = $700/day profit

        **$21K/month profit from gift card arbitrage.**
        """)

    st.markdown("---")

    st.subheader("Where to Sell Gift Cards for Cash")

    render(pd.DataFrame({
        "Place": ["CardTrader.com", "r/giftcardexchange (Reddit)", "Telegram gift card groups", "Local cash meet", "Facebook Marketplace", "eBay"],
        "Speed": ["Fast (instant)", "Medium (negotiate)", "Fast", "Fast", "Medium", "Slow"],
        "Discount You Get": ["10-20%", "10-20%", "10-20%", "10-15%", "10-15%", "5-15%"],
        "Your ID": ["Account needed", "Account needed", "None", "None", "None", "Some"],
    }))

    st.markdown("---")

    st.subheader("Flights and Hotels — Travala")

    st.markdown("""
**Travala.com** — USDT accepted directly.
- 2M+ hotels worldwide
- 600+ airlines
- No ID needed under $3,000
- 0% fee for USDT payments

**How to flip:**
1. Buy a $2,000 hotel booking with USDT on Travala
2. Sell the booking voucher to a traveler for $1,700 cash
3. Profit: $300

**Gamblers sometimes want these too** — people who can't pay online for whatever reason.
""")

    st.markdown("---")

    st.warning("⚠️ **Bitrefill was hacked March 2026.** 18,500 customer records exposed. Use CoinGate instead.")

# ─── PAGE 6: PRIVACY STACK ───────────────────────────────────────────────────
def page_privacy():
    st.title("🛡️ Privacy Stack — Ranked")
    st.subheader("Most private → Least private. Use the top ones first.")
    st.markdown("---")

    render(pd.DataFrame({
        "Rank": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "Method": ["Local P2P (in person)", "Gnosis Safe + Gnosis Pay", "DEX → BTC → P2P cash", "Gift cards → resell", "Flights/hotels → resell", "P2P on platform", "Loan (debt)", "Crypto debit cards"],
        "Privacy": ["🟢🟢🟢 Highest", "🟢🟢 High", "🟢🟢 High", "🟢🟢 High", "🟢🟢 High", "🟡 Medium", "🟡 Medium", "🔴 Low"],
        "ID Needed": ["None", "None", "None", "Email only", "No (<$3K)", "None", "Yes (loan)", "ID + selfie"],
        "Scale": ["Small", "Large", "Large", "Large", "Medium", "Unlimited", "Large", "Large"],
        "Risk": ["Trust-based", "None", "DEX slippage", "Gift card resale", "Booking resale", "AML watch", "Credit report", "Company has your ID"],
    }))

    st.markdown("---")

    st.subheader("The Privacy Rules")

    rules = [
        ("Cash is king", "Physical cash is untraceable. In-person P2P is the most private."),
        ("Your wallet, your rules", "Gnosis Safe = no company holds your money. No one can freeze it."),
        ("Under $10K cash", "Bank SARs trigger at $10,000+ in one cash deposit. Keep trades smaller."),
        ("Under $1K on-chain", "FATF Travel Rule means data travels with transactions over $1,000."),
        ("One wallet per purpose", "Don't mix wallets. Fresh wallet for large transfers."),
        ("Debt is invisible", "A loan shows on your credit report but the bank has no idea it's crypto-backed."),
        ("Gift cards are cash proxies", "Buy with USDT, sell for cash. Gamblers pay premium for convenience."),
    ]

    for title, desc in rules:
        st.markdown(f"**{title}:** {desc}")

    st.markdown("---")

    st.subheader("What Triggers Attention")

    render(pd.DataFrame({
        "Thing": ["$10K+ cash deposit", "$1K+ on-chain transfer", "Exchanging USDT for BTC", "Large P2P volume", "New bank account receiving wire"],
        "Triggers": ["Bank files SAR automatically", "Travel Rule kicks in, ID required", "Exchange may require KYC", "Platform monitors for AML", "Bank may ask questions"],
        "How to Avoid": ["Keep trades under $10K", "Break into smaller chunks", "Use DEX (no ID)", "Get FinCEN MSB + MTL", "Use an existing account"],
    }))

# ─── PAGE 7: FRAUD CASES ────────────────────────────────────────────────────
def page_fraud():
    st.title("⚠️ How They Got Caught")
    st.subheader("Real cases. Learn what NOT to do.")
    st.markdown("---")

    cases = [
        ("Crypto Dispensers — Nov 2025", "$10M alleged money laundering", "Ran cash-to-BTC ATMs. Banks flagged cash deposits. FBI traced money through ATMs.", "Cash deposits trigger SARs. Every ATM transaction is on-chain."),
        ("Paxful — Dec 2025", "$7.5M fine + platform shut down", "One of world's largest P2P platforms. No MTL licenses. No KYC/AML. Knew scammers used platform.", "You're responsible for what happens on your platform. Get licensed."),
        ("Samourai Wallet — 2025", "CEO: 60 months prison", "Privacy mixing wallet. Explicit money laundering intent.", "Privacy tools = treated as intent to hide money."),
        ("Ronald Spektor — Dec 2025", "$16M fraud, Brooklyn DA indictment", "Impersonated Coinbase support. Got victims to send crypto.", "Scamming = prison. But: ignoring scams on your platform = also prison."),
        ("Tether Freezes — 2025-2026", "$700M+ frozen", "Tether froze USDT connected to fraud. DOJ request.", "Tether can freeze your USDT instantly. No warning."),
        ("BTC ATM Fraud — 2025", "$333M lost, FBI report", "45K BTC ATMs in US. Scammers used them to receive payments.", "Bank accounts from ATM deposits = flagged immediately."),
        ("Operation Atlantic — May 2026", "276 arrests, $701M seized", "US + China + Canada coordinated crackdown.", "International law enforcement is highly coordinated now."),
    ]

    for name, amount, what, lesson in cases:
        with st.expander(f"{name} — {amount}"):
            st.markdown(f"**What happened:** {what}")
            st.error(f"**Lesson:** {lesson}")

    st.markdown("---")

    st.subheader("How They ALL Got Caught")

    render(pd.DataFrame({
        "Method": ["Blockchain tracing", "Bank SAR filings", "Exchange subpoenas", "Tether freezing", "Victim reports to FBI"],
        "Used In": ["Every case", "ATM fraud, cash deposits", "Paxful, exchanges", "All Tether cases", "Every scam case"],
        "What It Is": ["Chainalysis/TRM trace wallet history", "Bank reports suspicious activity to FinCEN", "Government subpoena → exchange gives up KYC", "Tether freezes on DOJ/OFAC request", "FBI IC3 complaints start investigations"],
    }))

    st.markdown("---")

    st.subheader("How to NOT Be Them")

    render(pd.DataFrame({
        "Do": ["Get FinCEN MSB if doing serious volume", "Basic KYC on platform users", "File SARs when something looks wrong", "Don't touch funds you suspect are stolen", "Keep records of all trades", "Don't mix wallets"],
        "Don't": ["Run P2P at scale without MTL", "Ignore red flag transactions", "Accept large cash without questions", "Use privacy mixers", "Skip compliance entirely", "Assume offshore = safe"],
    }))

    st.markdown("---")

    st.error("**Bottom line:** Every case above started with someone thinking they were protected. At $10M in volume — you're visible. Get some basic compliance. It's not that hard and it keeps you free.")

# ─── PAGE 8: APPS ──────────────────────────────────────────────────────────────
def page_apps():
    st.title("📱 The Apps — All in One Place")
    st.subheader("What to download. What to use. How to stay private.")
    st.markdown("---")

    st.subheader("Private First (No ID)")

    render(pd.DataFrame({
        "App": ["Gnosis Safe", "CoinGate", "MetaMask", "Trust Wallet", "Travala", "Telegram", "LocalCoinSwap"],
        "What It's For": ["Spend USDT directly, most private", "Gift cards with email only", "DEX swaps, wallet", "Backup wallet", "Flights + hotels with USDT", "P2P matching with gamblers", "Decentralized P2P, escrow built-in"],
        "ID Required": ["None", "Email only", "None", "None", "No (<$3K)", "None", "None"],
        "Website": ["safe.global", "coingate.com", "metamask.io", "trustwallet.com", "travala.com", "telegram.org", "localcoinswap.com"],
    }))

    st.markdown("---")

    st.subheader("Loans (Has Your ID)")

    render(pd.DataFrame({
        "App": ["Ledn", "Unchained Capital", "Lava Finance", "CoinRabbit"],
        "What It's For": ["Loan against BTC/ETH", "Loan against BTC", "Loan against BTC", "Loan against multi-asset"],
        "Collateral": ["BTC / ETH", "BTC / ETH", "BTC", "130+ assets"],
        "Output": ["USD wire", "USD wire", "USD wire", "USD wire"],
        "Website": ["ledn.io", "unchainedcapital.com", "lava.finance", "coinrabbit.io"],
    }))

    st.markdown("---")

    st.subheader("Semi-Private (ID on File)")

    render(pd.DataFrame({
        "App": ["Bleap", "RedotPay", "NoOnes", "SuisseGold (>$11K)"],
        "What It's For": ["Spend USDT anywhere, 2% cashback", "High limits, US Visa BIN", "P2P platform", "Physical gold with USDT"],
        "ID Needed": ["Gov ID + selfie", "Gov ID + selfie", "Account needed", "Gov ID + proof of address"],
        "Website": ["bleap.finance", "redotpay.com", "noones.com", "suissegold.com"],
    }))

    st.markdown("---")

    st.subheader("Gift Card Resale Markets")

    render(pd.DataFrame({
        "Place": ["CardTrader.com", "r/giftcardexchange", "Telegram GC groups", "eBay"],
        "What": ["P2P gift card marketplace", "Reddit community", "Direct to buyers", "Sell to strangers"],
        "Your ID": ["Account", "Account", "None", "Some"],
    }))

    st.markdown("---")

    st.subheader("The Daily Stack")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **Morning:**
        - Check Telegram P2P groups
        - Match 5-10 gambler trades
        - Confirm cash received
        - Release USDT
        """)
    with col2:
        st.markdown("""
        **Afternoon:**
        - Buy gift cards on CoinGate
        - Post on CardTrader / Telegram
        - Sell to gamblers
        - Collect cash
        """)
    with col3:
        st.markdown("""
        **Ongoing:**
        - Gnosis Safe for spending
        - Build relationships with repeat buyers
        - Scale P2P volume
        - Track all trades
        """)

# ─── APP SHELL ────────────────────────────────────────────────────────────────
PAGES = {
    "🏠 Home": page_home,
    "🤝 P2P Gamblers": page_p2p,
    "💳 Loan (Debt = Not Income)": page_loans,
    "🔐 Gnosis Safe (Most Private)": page_safe,
    "🎁 Gift Cards + Flights": page_gift,
    "🛡️ Privacy Stack": page_privacy,
    "⚠️ Fraud Cases": page_fraud,
    "📱 All Apps": page_apps,
}

st.sidebar.title("💸 USDT → Cash")
st.sidebar.caption("Privacy ranked. No government ID.")

selection = st.sidebar.radio("Navigate", list(PAGES.keys()), label_visibility="collapsed")
PAGES[selection]()