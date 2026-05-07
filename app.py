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

def section(title, body):
    st.subheader(title)
    st.markdown(body)

# ─── PAGE 1: HOME ────────────────────────────────────────────────────────────────
def page_home():
    st.title("💸 USDT → Cash")
    st.subheader("How to turn USDT into cash. No government ID. Ranked by method.")
    st.markdown("---")

    st.success("""
**The goal:** $10M in USDT. Get it out as cash. No government ID. No bank needed.

**Two angles:**
- **P2P gambling business** — match gamblers to cash, take the spread
- **Collateral loan** — put up USDT, get cash, bank sees debt not income
""")

    st.markdown("---")
    st.subheader("All Ways to Get USDT → Cash")

    render(pd.DataFrame({
        "Method": [
            "🤝 P2P — Gamblers buy crypto",
            "👤 Local P2P — In person cash",
            "🎁 Gift Cards — Buy, resell for cash",
            "✈️ Flights/Hotels — Buy, resell",
            "💱 DEX → BTC → cash meet",
            "💳 Loan — Put up USDT as collateral",
            "🔐 Gnosis Safe — Spend directly",
        ],
        "Output": [
            "Cash via platform escrow",
            "Cash in hand",
            "Cash from reselling",
            "Cash from reselling",
            "Cash in hand",
            "Wire to bank OR cash",
            "Spend anywhere",
        ],
        "ID Needed": [
            "None",
            "None",
            "Email only",
            "No (under $3K)",
            "None",
            "Yes (loan companies)",
            "None",
        ],
        "Best For": [
            "Main business — gamblers",
            "Most private",
            "Gamblers want gift cards",
            "Gamblers need travel",
            "Privacy first",
            "Large amounts",
            "Spending, not selling",
        ],
    }))

    st.markdown("---")
    st.subheader("The Privacy Stack")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Most Private", "Local P2P", "Cash in hand")
    c2.metric("Best Tech", "Gnosis Safe", "No one holds it")
    c3.metric("Business", "P2P Gamblers", "Main income")
    c4.metric("Bank Cash", "Loan", "Debt not income")

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

    st.code("""
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
""", language=None)

    st.markdown("---")
    st.subheader("Where to Find Gamblers")

    render(pd.DataFrame({
        "Place": ["Telegram P2P groups", "LocalCoinSwap.com", "NoOnes.com", "Build your own platform", "LocalBitcoin meetups", "Craigslist / FB Marketplace"],
        "What": ["Crypto signal groups, gambling groups", "Decentralized P2P, escrow built-in", "Decentralized P2P, Telegram integration", "Build your own app or website", "In-person cash meets", "Local cash sellers"],
        "Scale": ["Medium", "High", "High", "Unlimited", "Small", "Small"],
        "Your ID": ["None", "None", "None", "None", "None", "None"],
    }))

    st.markdown("---")
    st.subheader("Step by Step")

    steps = [
        ("1", "Get a wallet", "Download Trust Wallet or MetaMask. 5 minutes."),
        ("2", "Join Telegram groups", "Search: crypto P2P, USDt buy, betting crypto. Join gambling communities."),
        ("3", "Post an ad", "Say: buying USDT, paying cash, 2% below market."),
        ("4", "Match buyer and seller", "Connect gambler to USDT holder. Hold USDT in escrow."),
        ("5", "Confirm cash receipt", "Once cash lands, release the USDT."),
        ("6", "Keep the spread", "You made 2-5% on the trade. Repeat."),
    ]
    for num, title, desc in steps:
        c1, c2 = st.columns([1, 5])
        c1.markdown(f"**{num}**")
        c2.markdown(f"**{title}** — {desc}")

    st.markdown("---")
    st.subheader("What Gamblers Want")

    render(pd.DataFrame({
        "What": ["USDT", "Steam Cards", "Amazon Cards", "Apple Cards", "Google Play", "Skrill / Neteller", "Flight / Hotel bookings"],
        "Why": ["For betting sites directly", "Skin gambling sites", "Sell for cash on marketplaces", "Buy apps / sell for cash", "Buy apps / sell for cash", "Direct deposit to betting accounts", "Resell for cash at discount"],
        "Spread You Can Take": ["2-5%", "10-20%", "10-15%", "10-15%", "10-15%", "5-10%", "10-20%"],
    }))

    st.markdown("---")
    st.subheader("Scaling Up")

    st.markdown("""
**Start:** Telegram + wallet = $0 to start
**Scale:** Build a P2P website or app

**What a platform does:** Escrow, user verification (optional), payment rails, dispute resolution, volume tracking

**Technology:** White-label P2P software, NoOnes/LocalCoinSwap API, or build from scratch

**No ID needed** at small scale. At serious volume: FinCEN MSB + Wyoming MTL.
""")

    st.warning("Paxful was shut down Dec 2025. $7.5M fine. No MTL licenses. No AML program. Get licensed before doing serious volume.")

# ─── PAGE 3: LOANS ─────────────────────────────────────────────────────────────
def page_loans():
    st.title("💳 Loan — Put Up USDT, Get Cash")
    st.subheader("Two paths: bank wire or cash in hand. Both work.")
    st.markdown("---")

    st.success("""
**The key insight:** A loan against your USDT is DEBT, not income.

The bank sees: personal loan from a company
The IRS sees: debt
You see: cash in your account

**No capital gains tax. No income tax. Banks don't ask about your collateral.**
""")

    st.markdown("---")
    st.subheader("Path 1: Bank Wire (Need Some ID)")

    st.markdown("""
**Best for:** Getting large amounts into a bank account cleanly

```
USDT
  ↓
Swap USDT → BTC/ETH (one taxable event, pay once)
  ↓
Put BTC/ETH as collateral at Ledn / Unchained
  ↓
They wire USD to your bank
  ↓
Bank sees: personal loan from Ledn Capital
```

**Bank sees:**
```
Wire transfer: personal loan
Source: Ledn Capital
```
**That's it. They don't see your USDT.**
""")

    render(pd.DataFrame({
        "Platform": ["Ledn", "Unchained Capital", "Lava Finance", "CoinRabbit"],
        "Collateral": ["BTC / ETH", "BTC / ETH", "BTC", "Multi-asset"],
        "LTV": ["50%", "50%", "50%", "50%"],
        "APR": ["9.99-11.49%", "12-15%", "~5%", "8-16%"],
        "Output": ["USD wire", "USD wire", "USD wire", "USD wire"],
        "ID Needed": ["Yes", "Yes", "Some", "Yes"],
    }))

    st.markdown("---")
    st.subheader("Path 2: Cash (No Bank, No ID on the Loan)")

    st.markdown("""
**Best for:** Keeping everything private, no bank involved

```
USDT
  ↓
Deposit into Aave V3 or Morpho Blue (no ID needed)
  ↓
Borrow USDC (instant, no ID)
  ↓
Send USDC to SimpleSwap / Exolix (no ID needed)
  ↓
USDC → USD via their P2P or swap
  ↓
Cash in hand OR wire to your bank
```

**SimpleSwap and Exolix are no-KYC exchanges.**
They send the wire. The bank sees: wire from SimpleSwap.
**No one knows it was your USDT.**
""")

    render(pd.DataFrame({
        "Platform": ["Aave V3", "Morpho Blue", "SimpleSwap", "Exolix", "StealthEX"],
        "Role": ["Borrow USDC against USDT", "Borrow USDC against ETH", "No-KYC off-ramp USDC→USD", "No-KYC off-ramp USDC→USD", "No-KYC off-ramp USDC→USD"],
        "Collateral": ["USDT / ETH / wstETH", "ETH / USDC", "None", "None", "None"],
        "ID Needed": ["None", "None", "None", "None", "None"],
        "Output": ["USDC (on-chain)", "USDC (on-chain)", "Wire / cash / crypto", "Wire / cash / crypto", "Wire / crypto"],
        "Notes": ["Primary DeFi option", "Better rates than Aave", "Best no-KYC off-ramp", "Fast, no account", "800+ coins"],
    }))

    st.markdown("---")
    st.subheader("What the Bank Actually Sees")

    render(pd.DataFrame({
        "Scenario": ["Loan from Ledn (Path 1)", "Wire from SimpleSwap (Path 2)", "Cash in person (any method)"],
        "Bank Sees": ["Personal loan from Ledn Capital", "Wire from SimpleSwap", "Nothing — cash in your pocket"],
        "IRS Sees": ["Debt (not income)", "Not reported", "Not reported"],
        "Red Flags": ["None", "None (looks like normal wire)", "None — most private"],
    }))

    st.markdown("---")
    st.subheader("The USDT Problem")

    st.markdown("""
Most loan platforms want BTC or ETH as collateral, not USDT.

**Solution:** One swap USDT → BTC/ETH, then take the loan.
- One taxable event (you sold USDT)
- Pay the small tax once
- Then borrow against BTC

**OR just use the cash methods** (P2P, gift cards, local meet) — no swap needed, no tax event.
""")

# ─── PAGE 4: CASH ONLY ───────────────────────────────────────────────────────
def page_cash():
    st.title("💵 Cash Only — No Bank Involved")
    st.subheader("Every way to get USDT → cash in your hand. No wire. No bank. No SARs.")
    st.markdown("---")

    render(pd.DataFrame({
        "Method": ["Local P2P in person", "Gift cards → resell", "Flights / hotels → resell", "DEX → BTC → cash meet", "P2P platform escrow"],
        "ID Needed": ["None", "Email only", "No (under $3K)", "None", "None"],
        "Cash Speed": ["Instant", "Same day", "Same day", "Same day", "Same day"],
        "Best For": ["Most private", "Gamblers want cards", "Gamblers need travel", "Privacy first", "Scaling up"],
    }))

    st.markdown("---")
    st.subheader("Local P2P In Person")

    st.markdown("""
**Most private method. Cash in hand. No one knows.**

```
Gambler wants USDT
     ↓
Agree on price (usually 2-5% below market)
     ↓
Meet at bank or coffee shop
     ↓
They hand you cash
     ↓
You send USDT to their wallet
     ↓
Walk away
```

**No app needed.** Trust-based. Build repeat relationships.
""")

    st.markdown("---")
    st.subheader("Gift Cards → Resell for Cash")

    st.markdown("""
**CoinGate.com:** Email only. No ID. Buy gift cards with USDT.

```
USDT → CoinGate (buy Steam card / Amazon / Apple)
     ↓
Sell to gambler for 85 cents on the dollar
     ↓
Cash in your pocket
```

**Steam cards** = skin gambling sites. Gamblers pay premium.
**Amazon / Apple** = sell on CardTrader.com or Reddit for cash.
**Profit per card:** 10-20% of face value.
""")

    st.markdown("---")
    st.subheader("Flights and Hotels → Resell")

    st.markdown("""
**Travala.com:** No ID under $3K. Buy flights and hotels with USDT.

```
USDT → Travala (buy hotel booking)
     ↓
Sell the booking voucher to a traveler for 20% below
     ↓
Cash in your pocket
```

**Gamblers sometimes want this too** — people who can't pay online for whatever reason.
""")

    st.markdown("---")
    st.subheader("DEX → BTC → Cash Meet")

    st.markdown("""
**When you want BTC instead of USDT:**

```
USDT → Uniswap / THORSwap → BTC
     ↓
Post on NoOnes / LocalCoinSwap: selling BTC
     ↓
Buyer pays you cash in person
     ↓
Send BTC to their wallet
```

**Banks see nothing.** Cash in your hand. BTC sale paper trail is separate from USDT.
""")

    st.markdown("---")
    st.subheader("The Math — Gift Card Example")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **Steam Cards**
        1. Buy $1,000 Steam card on CoinGate for $1,000 USDT
        2. Sell to gambler for $850 cash
        3. Profit: $150
        4. Gambler gets $1K gambling credits for $850

        **Win-win.**
        """)
    with c2:
        st.markdown("""
        **Scale: 10 cards/day**
        - 10 × $1,000 Steam cards = $10,000 USDT
        - Sell each for $850 = $8,500 cash
        - Daily profit: $1,500
        - Monthly: $45,000 profit

        **No bank. No ID. Cash in your pocket.**
        """)

# ─── PAGE 5: GNOSIS SAFE ────────────────────────────────────────────────────
def page_safe():
    st.title("🔐 Gnosis Safe — Spend USDT Directly")
    st.subheader("Most private. Your wallet. No company holds it. No one can freeze it.")
    st.markdown("---")

    st.success("""
**The key:** Your USDT never leaves your wallet.

Unlike Bleap or RedotPay where a company holds your USDT — with Gnosis Safe, you spend directly from your own wallet.

No company = no one to freeze your money = most private.
""")

    st.markdown("---")
    st.subheader("What Happens")

    st.code("""
YOUR GNOSIS SAFE WALLET ($10M USDT)
        ↓
Gnosis Pay creates a virtual Visa card linked to your wallet
        ↓
You buy something for $500
        ↓
Gnosis Pay checks: is there enough in the Safe? Yes.
        ↓
3-minute window to cancel
        ↓
Transaction settles from YOUR wallet
        ↓
Merchant gets USD
YOU NEVER SOLD ANYTHING
""", language=None)

    st.markdown("---")
    st.subheader("What You Can Do")

    render(pd.DataFrame({
        "What": ["Online shopping (Amazon, anything)", "In-store NFC tap to pay", "ATM withdrawals", "Bank transfer to another account", "Pay contractors directly", "No 1099 issued", "No company can freeze your money"],
        "How": ["Visa accepted anywhere", "Apple Pay / Google Pay", "Compatible ATMs worldwide", "Send from your wallet", "Send USDT to their wallet", "It's your wallet, not theirs", "True self-custody"],
    }))

    st.markdown("---")
    st.subheader("vs Other Cards")

    render(pd.DataFrame({
        "Feature": ["Who holds your USDT?", "Can they freeze it?", "Do they have your ID?", "IRS reporting?", "Best for"],
        "Bleap": ["Bleap company", "Yes", "Yes (ID + selfie)", "Yes", "Easy spending"],
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
        c1, c2 = st.columns([1, 5])
        c1.markdown(f"**{num}**")
        c2.markdown(f"**{title}** — {desc}")

    st.warning("Limitation: Mostly EU/EEA right now. US rollout coming. Check if it works in your country.")

# ─── PAGE 6: GIFT CARDS + TRAVEL ─────────────────────────────────────────────
def page_gift():
    st.title("🎁 Gift Cards + Flights — Resell for Cash")
    st.subheader("Buy with USDT. Sell to gamblers. Cash in your pocket.")
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
""")

    st.warning("Bitrefill was hacked March 2026. 18,500 customer records exposed. Use CoinGate instead.")

# ─── PAGE 7: PRIVACY STACK ───────────────────────────────────────────────────
def page_privacy():
    st.title("🛡️ Privacy Stack — Ranked")
    st.subheader("Most private → Least private. Use the top ones first.")
    st.markdown("---")

    render(pd.DataFrame({
        "Rank": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "Method": ["Local P2P (in person)", "Gnosis Safe + Gnosis Pay", "DEX to BTC to cash meet", "Gift cards to resell", "Flights/hotels to resell", "P2P on platform", "Loan (debt)", "Crypto debit cards"],
        "ID Needed": ["None", "None", "None", "Email only", "No (<$3K)", "None", "Yes (loan company)", "ID + selfie"],
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

# ─── PAGE 8: FRAUD CASES ────────────────────────────────────────────────────
def page_fraud():
    st.title("⚠️ How They Got Caught")
    st.subheader("Real cases. Learn what NOT to do.")
    st.markdown("---")

    cases = [
        ("Crypto Dispensers — Nov 2025", "$10M alleged money laundering", "Ran cash-to-BTC ATMs. Banks flagged cash deposits. FBI traced money through ATMs.", "Cash deposits trigger SARs. Every ATM transaction is on-chain."),
        ("Paxful — Dec 2025", "$7.5M fine + platform shut down", "One of world's largest P2P platforms. No MTL licenses. No KYC/AML. Knew scammers used platform.", "You're responsible for what happens on your platform. Get licensed."),
        ("Samourai Wallet — 2025", "CEO: 60 months prison", "Privacy mixing wallet. Explicit money laundering intent.", "Privacy tools = treated as intent to hide money."),
        ("Ronald Spektor — Dec 2025", "$16M fraud, Brooklyn DA indictment", "Impersonated Coinbase support. Got victims to send crypto.", "Scamming = prison. Ignoring scams on your platform = also prison."),
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
        "What It Is": ["Chainalysis/TRM trace wallet history", "Bank reports suspicious activity to FinCEN", "Government subpoena: exchange gives up KYC", "Tether freezes on DOJ/OFAC request", "FBI IC3 complaints start investigations"],
    }))

    st.markdown("---")
    st.subheader("How to NOT Be Them")

    render(pd.DataFrame({
        "Do": ["Get FinCEN MSB if doing serious volume", "Basic KYC on platform users", "File SARs when something looks wrong", "Do not touch funds you suspect are stolen", "Keep records of all trades", "Do not mix wallets"],
        "Don't": ["Run P2P at scale without MTL", "Ignore red flag transactions", "Accept large cash without questions", "Use privacy mixers", "Skip compliance entirely", "Assume offshore = safe"],
    }))

    st.error("Bottom line: At $10M in volume, you are visible. Get some basic compliance. It's not that hard and it keeps you free.")

# ─── PAGE 9: APPS ──────────────────────────────────────────────────────────────
def page_apps():
    st.title("📱 The Apps — All in One Place")
    st.subheader("What to download. What to use. No government ID where possible.")
    st.markdown("---")

    st.subheader("Private First (No ID)")

    render(pd.DataFrame({
        "App": ["Gnosis Safe", "CoinGate", "MetaMask", "Trust Wallet", "Travala", "Telegram", "SimpleSwap", "Exolix"],
        "What It's For": ["Spend USDT directly, most private", "Gift cards with email only", "DEX swaps, wallet", "Backup wallet", "Flights + hotels with USDT", "P2P matching with gamblers", "No-KYC USDC to wire/cash", "No-KYC USDC to wire/cash"],
        "ID Needed": ["None", "Email only", "None", "None", "No (<$3K)", "None", "None", "None"],
        "Website": ["safe.global", "coingate.com", "metamask.io", "trustwallet.com", "travala.com", "telegram.org", "simpleswap.io", "exolix.com"],
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
        "App": ["Bleap", "RedotPay", "NoOnes", "LocalCoinSwap"],
        "What It's For": ["Spend USDT anywhere, 2% cashback", "High limits, US Visa BIN", "P2P platform", "Decentralized P2P, escrow built-in"],
        "ID Needed": ["Gov ID + selfie", "Gov ID + selfie", "Account needed", "Account needed"],
        "Website": ["bleap.finance", "redotpay.com", "noones.com", "localcoinswap.com"],
    }))

    st.markdown("---")
    st.subheader("The Daily Stack")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        **Morning:**
        - Check Telegram P2P groups
        - Match 5-10 gambler trades
        - Confirm cash received
        - Release USDT
        """)
    with c2:
        st.markdown("""
        **Afternoon:**
        - Buy gift cards on CoinGate
        - Post on CardTrader / Telegram
        - Sell to gamblers
        - Collect cash
        """)
    with c3:
        st.markdown("""
        **Ongoing:**
        - Gnosis Safe for spending
        - Build repeat buyer relationships
        - Scale P2P volume
        - Track all trades
        """)

# ─── APP SHELL ────────────────────────────────────────────────────────────────
PAGES = {
    "🏠 Home": page_home,
    "🤝 P2P Gamblers": page_p2p,
    "💳 Loan": page_loans,
    "💵 Cash Only": page_cash,
    "🔐 Gnosis Safe": page_safe,
    "🎁 Gift Cards + Travel": page_gift,
    "🛡️ Privacy Stack": page_privacy,
    "⚠️ Fraud Cases": page_fraud,
    "📱 All Apps": page_apps,
}

st.sidebar.title("💸 USDT → Cash")
st.sidebar.caption("No government ID. No bank needed.")

selection = st.sidebar.radio("Navigate", list(PAGES.keys()), label_visibility="collapsed")
PAGES[selection]()