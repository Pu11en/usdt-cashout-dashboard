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

# ─── PAGE 1: HOME ────────────────────────────────────────────────────────────────
def page_home():
    st.title("💸 USDT → Cash")
    st.subheader("How to turn USDT into cash. No government ID. Ranked by method.")
    st.markdown("---")

    st.success("""
**The goal:** USDT in your wallet. Cash in your pocket. No government ID. No one keeping a file on you.

**How it works:**
- People have cash and want USDT. You connect them. Take the spread.
- OR put up USDT as collateral. Get a loan. Bank sees debt — not income.
- OR buy things with USDT and sell them for cash.

**Three angles. All private. All real.**
""")

    st.markdown("---")
    st.subheader("All Ways to Get USDT → Cash")

    render(pd.DataFrame({
        "Method": [
            "🤝 P2P — Cash people want USDT",
            "👤 Local meet — Cash in hand",
            "💵 Goods arbitrage — Buy with USDT, sell for cash",
            "🎁 Gift cards — Buy with USDT, sell for cash",
            "✈️ Travel — Buy bookings, resell",
            "💳 Loan — Collateral becomes debt",
            "🔐 Gnosis Safe + Pay — Debit card (EU/LatAm residency)",
            "💱 DEX → off-ramp — Swap, wire, cash",
        ],
        "Output": [
            "Cash via platform escrow",
            "Cash in hand",
            "Cash from reselling",
            "Cash from reselling",
            "Cash from reselling",
            "Wire or cash",
            "Spend anywhere",
            "Wire or cash",
        ],
        "ID Needed": [
            "None",
            "None",
            "None",
            "Email only",
            "No (<$3K)",
            "Yes (loan company)",
            "Residency (EU/LatAm)",
            "None",
        ],
        "Best For": [
            "Main business — scale up",
            "Most private",
            "Large items",
            "Quick turnaround",
            "People who need travel",
            "Large amounts to bank",
            "Daily spending",
            "Privacy route",
        ],
    }))

    st.markdown("---")
    st.subheader("The Three Angles")

    st.markdown("---")
    st.subheader("The Reality Check")

    st.warning("""
**No wallet-to-card shortcut exists in 2026.** You cannot go USDT wallet → debit card directly without KYC. Every card issuer (Visa, Mastercard) requires identity verification by law. SolCard was the last no-KYC option and they removed it April 2026.

**The only path to a bank debit card:** USDT → swap to BTC → collateral at Ledn/Unchained → wire to bank → bank debit card.

**OR use the cash methods:** P2P, gift cards, goods arbitrage, Gnosis Safe spending.
""")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        **1. P2P Business**
        Connect cash people to USDT people.
        Take 2-5% on every trade.
        Scale from Telegram to platform.
        """)
    with c2:
        st.markdown("""
        **2. Goods Arbitrage**
        Buy things with USDT.
        Sell them for cash.
        Flips, cars, hotels, anything.
        """)
    with c3:
        st.markdown("""
        **3. Loan Route**
        Put USDT as collateral.
        Get debt — not income.
        Wire to any bank.
        """)

# ─── PAGE 2: P2P ────────────────────────────────────────────────────────────────
def page_p2p():
    st.title("🤝 P2P — Connect Cash People to USDT People")
    st.subheader("The main business. Someone has cash. They want USDT. You match them. Take the spread.")
    st.markdown("---")

    st.success("""
**The model:**
- Someone has cash. They want USDT instead of cash.
- Another person has USDT and wants cash.
- You match them. Cash goes to the seller. USDT goes to the buyer. You take a %.

Why do they want it? Doesn't matter. Some want to hold stablecoins. Some gamble.
Some just don't trust banks. That's not your business.

Your business: connect cash to crypto. Take the fee.

**No government ID needed on your end. Just a wallet and Telegram.**
""")

    st.markdown("---")
    st.subheader("How It Works")

    st.code("""
SOMEONE (has cash, wants USDT)
     ↓
YOU match them with a USDT HOLDER
     ↓
USDT holder sends USDT to buyer's wallet
     ↓
Cash goes to the USDT holder
     ↓
You take 2-5% of every trade
YOUR USDT NEVER MOVES.
""", language=None)

    st.markdown("---")
    st.subheader("Where to Find People")

    render(pd.DataFrame({
        "Place": ["Telegram", "LocalCoinSwap.com", "NoOnes.com", "Build your own platform", "Local meetups", "Craigslist / FB Marketplace"],
        "What": ["Crypto groups, anyone wanting USDT", "Decentralized P2P, escrow built-in", "Decentralized P2P, Telegram integration", "Build your own app or website", "In-person cash meets", "Local cash sellers"],
        "Scale": ["Medium", "High", "High", "Unlimited", "Small", "Small"],
        "Your ID": ["None", "None", "None", "None", "None", "None"],
    }))

    st.markdown("---")
    st.subheader("Step by Step")

    steps = [
        ("1", "Get a wallet", "Download Trust Wallet or MetaMask. 5 minutes."),
        ("2", "Join Telegram groups", "Search: crypto P2P, USDt buy. Find anyone with cash who wants USDT."),
        ("3", "Post an ad", "Say: facilitating trades, small fee per transaction."),
        ("4", "Match buyer and seller", "Connect buyer to USDT holder. Hold USDT in escrow."),
        ("5", "Confirm cash receipt", "Once cash lands, release the USDT."),
        ("6", "Keep the spread", "You made 2-5% on the trade. Repeat."),
    ]
    for num, title, desc in steps:
        c1, c2 = st.columns([1, 5])
        c1.markdown(f"**{num}**")
        c2.markdown(f"**{title}** — {desc}")

    st.markdown("---")
    st.subheader("What People Want")

    render(pd.DataFrame({
        "What": ["USDT", "Steam Cards", "Amazon Cards", "Apple Cards", "Google Play", "Skrill / Neteller", "Flight / Hotel bookings"],
        "Why": ["Hold stablecoins instead of cash", "Sell for cash / use on sites", "Sell for cash on marketplaces", "Buy apps / sell for cash", "Buy apps / sell for cash", "Direct deposit to accounts", "Resell for cash at discount"],
        "Spread You Can Take": ["2-5%", "10-20%", "10-15%", "10-15%", "10-15%", "5-10%", "10-20%"],
    }))

    st.markdown("---")
    st.subheader("Scaling Up")

    st.markdown("""
**Start:** Telegram + wallet = $0 to start

**Scale:** Build a P2P website or app

**What a platform does:** Escrow, payment rails, dispute resolution, volume tracking

**At scale:** FinCEN MSB registration + Wyoming MTL before doing serious volume.

**This is a real business. People pay premium for fast, private crypto trades.**
""")

    st.warning("Paxful shut down Nov 2025. $3.5-4M fine. No MTL licenses. No AML program. Get licensed before doing serious volume.")

# ─── PAGE 3: LOANS ─────────────────────────────────────────────────────────────
def page_loans():
    st.title("💳 Loan — Collateral Becomes Debt")
    st.subheader("Put up USDT. Get a loan. Bank sees debt. Not income. Not taxable.")
    st.markdown("---")

    st.success("""
**The key insight:** When you put up collateral and take a loan — it's DEBT, not income.

The bank sees: personal loan from a company
The IRS sees: debt
You see: cash in your account

**No capital gains. No income tax. Banks don't ask about your collateral.**
""")

    st.markdown("---")
    st.subheader("US Bank — Personal Loan (Simplest)")

    st.markdown("""
**Best for:** Getting large amounts into a US bank cleanly

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

**What bank sees:**
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
        "APR": ["9.99-11.49%", "9.5-16%", "5-7.5%", "8-16%"],
        "Output": ["USD wire", "USD wire", "USD wire", "USD wire"],
        "ID Needed": ["Yes", "Yes", "Some", "Yes"],
    }))

    st.markdown("---")
    st.subheader("Foreign Bank — No US Questions")

    st.markdown("""
**Best for:** If you have connections in foreign banking. Dollarized countries (Panama, UAE, etc.) see USD wires as completely normal.

```
USDT
  ↓
Swap to BTC (one taxable event, pay once)
  ↓
Use BTC as collateral at a loan platform OR
Use a bank that accepts stablecoin deposits (FV Bank)
  ↓
They wire USD to your foreign bank account
  ↓
Foreign bank sees: USD wire, debt on the books
No US tax. No US reporting.
```

**What banks in Panama, UAE, Cayman see:** A normal USD wire. They don't know or care about your USDT. USD is USD to them.

**Why foreign banks don't ask:** They're used to large USD wires from abroad. It's normal for them.
""")

    st.markdown("---")
    st.subheader("No-Bank Route — Cash in Hand")

    st.markdown("""
**Best for:** No bank involved at all. Cash only.

```
USDT
  ↓
Deposit into Aave V3 or Morpho Blue (no ID)
  ↓
Borrow USDC (instant, no ID)
  ↓
Send USDC to SimpleSwap (no ID)
  ↓
USDC → USD via their swap or P2P
  ↓
Cash in hand
```

**No bank. No statements. No records.**
""")

    st.markdown("---")
    st.subheader("What the Bank Actually Sees")

    render(pd.DataFrame({
        "Scenario": ["Loan from Ledn (US bank)", "Wire to foreign bank (Panama/UAE)", "Cash in hand (no bank)"],
        "Bank Sees": ["Personal loan from Ledn Capital", "USD wire from abroad", "Nothing — cash in your pocket"],
        "IRS Sees": ["Debt (not income)", "Not reported to US IRS", "Not reported"],
        "Questions Asked": ["None", "None in dollarized countries", "None"],
    }))

    st.markdown("---")
    st.warning("One swap = one taxable event. If you swap USDT to BTC to get a loan: pay the small tax on that one sale. Done. Everything after = no tax.")

    st.markdown("---")
    st.subheader("Bank Debit Card Route — Spend Normally After the Loan")

    st.markdown("""
**Once the loan money is in your bank account — you are just a normal person with a high balance.**

```
USDT
  | Swap to BTC (one tax event)
BTC as collateral at Ledn / Unchained
  |
They wire to your bank
  |
Bank sees: personal loan from Ledn Capital
  |
Request high-limit debit card from YOUR bank
  |
Spend anywhere. ATM. Normal bank card.
```

**Why this is the cleanest route:**
- The bank sees a personal loan — nothing crypto-related
- High balance = expected to have a high-limit debit card
- Daily spending of $10K-$50K is normal for this balance
- No crypto card. No no-KYC complications. Just a normal bank debit card.

**vs crypto cards:**

| | Bank Debit Card | Crypto Card (SolCard, Bleap) |
|---|---|---|
| Daily limit | $10K-$50K+ | $5K-$100K |
| ATM limit | $1K-$5K/day | Limited or none |
| Bank knows it is crypto? | No | Sometimes |
| Can they freeze it? | Only if suspicious | Yes — any time |
| Normal to have high limits? | Yes | They question it |

**Best banks for this:**
- **Cross River Bank** — already processes crypto company wires daily. Will not blink.
- **FV Bank (Puerto Rico)** — deposit USDC directly, or receive wire from Ledn. Crypto-aware.
- **Private bank (JP Morgan, Citi, Goldman)** — used to high balances. High-limit cards standard.
- **Your existing bank** — fewer questions if they know you.
""")

# ─── PAGE 4: GOODS ARBITRAGE ─────────────────────────────────────────────────
def page_goods():
    st.title("💵 Goods Arbitrage — Buy With USDT, Sell for Cash")
    st.subheader("Use USDT to buy things. Sell them for cash. Keep the spread.")
    st.markdown("---")

    st.success("""
**The model:**
1. Buy something with USDT
2. Find a buyer who will pay cash
3. Sell it for less than you paid — but they pay in cash
4. You got cash. They got what they wanted. Win-win.

**Works with: cars, watches, art, electronics, flights, hotels, anything.**
""")

    st.markdown("---")
    st.subheader("Flips and Cars")

    st.markdown("""
**Classic flip:** Buy a car with USDT. Sell it for cash.

```
USDT → Buy car ($50,000)
     ↓
List it for $47,000 cash
     ↓
Buyer pays you $47,000 cash
     ↓
You kept $47,000 cash
     ↓
USDT is gone. Cash in your pocket.
```

**No sale on the blockchain.** You bought a car. You sold a car. Normal transaction.

**Where to find buyers:** Private sales, dealers who take cash, anyone who can't or doesn't want to use their bank for large purchases.
""")

    st.markdown("---")
    st.subheader("Gift Cards (Fastest Turnaround)")

    st.markdown("""
**CoinGate.com:** Email only for small purchases. No government ID under certain limits. For larger transactions KYC may be required.

```
USDT → CoinGate (buy $1,000 Steam card)
     ↓
Post for sale: $850 cash
     ↓
Buyer pays $850 cash
     ↓
$850 cash in your pocket
```

**Profit per card:** 10-20% of face value.

**Steam cards:** People pay premium for gaming credits.
**Amazon / Apple:** Resell on CardTrader.com, Reddit, or directly.
**Gift cards = fastest cash turnaround.**
""")

    st.markdown("---")
    st.subheader("Flights and Hotels")

    st.markdown("""
**Travala.com:** USDT accepted directly. 2M+ hotels, 600+ airlines. No ID under $3,000.

```
USDT → Travala (buy $2,000 hotel booking)
     ↓
Sell the booking voucher for $1,700 cash
     ↓
$1,700 cash in your pocket
```

**Why this works:** Some people can't pay online with a card. Some prefer to pay someone directly. You provide that service.

**Profit:** 10-20% below face value.
""")

    st.markdown("---")
    st.subheader("What to Flip")

    render(pd.DataFrame({
        "Item": ["Gift cards (Steam, Amazon, Apple)", "Hotel bookings", "Flight bookings", "Cars", "Watches", "Electronics", "Art"],
        "Speed": ["Instant", "Same day", "Same day", "Days to weeks", "Days to weeks", "Days", "Days to weeks"],
        "Profit": ["10-20%", "10-20%", "10-20%", "5-15%", "5-20%", "5-15%", "Varies"],
        "Risk": ["Low", "Low", "Low", "Medium", "High value", "Low", "High value"],
        "Best For": ["Fast cash, repeatable", "People needing travel", "People needing travel", "Large amounts", "High-end items", "Quick cash", "Art collectors"],
    }))

    st.markdown("---")
    st.subheader("The Math")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **Gift Cards — Fast Scale**
        - 10 × $1,000 Steam cards = $10,000 USDT
        - Sell each for $850 = $8,500 cash
        - Daily profit: $1,500
        - Monthly: $45,000 profit

        No bank. No ID. Cash in your pocket.
        """)
    with c2:
        st.markdown("""
        **Cars — Large Amounts**
        - Buy $50,000 car with USDT
        - Sell for $47,000 cash
        - Profit: $47,000 cash
        - One flip = half your capital back as cash

        Slower but high volume.
        """)
    st.warning("Bitrefill was hacked March 2026. 18,500 customer records exposed. Use CoinGate instead.")

# ─── PAGE 5: GNOSIS SAFE ────────────────────────────────────────────────────
def page_safe():
    st.title("🔐 Gnosis Safe — Spend USDT Directly")
    st.subheader("Self-custody wallet. Spend via debit card. EU/LatAm residency required for card.")
    st.markdown("---")

    st.success("""
**What Gnosis Safe IS:**
- A self-custody wallet. You hold your USDT. No company can freeze it. Works globally. No ID to create.

**What Gnosis Pay (the card) REQUIRES:**
- EU or Latin American residency
- A bank account in a supported country (card settles in EUR)
- Your country is verified during card issuance
- NOT available in the US

**What it does NOT require:**
- No passport upload. No selfie. No government ID photo.
- But your bank account + residency effectively identify you.

**No 1099 from the card. No company controls your funds. But you are NOT anonymous — your bank knows who you are.**
""")

    st.markdown("---")
    st.subheader("How It Works")

    st.code("""
YOUR GNOSIS SAFE WALLET
        ↓
Gnosis Pay creates a virtual Visa debit card
        ↓
You buy something or withdraw from ATM
        ↓
Transaction settles from YOUR wallet
        ↓
Merchant gets USD. ATM gives you cash.
YOU NEVER SOLD ANYTHING.
""", language=None)

    st.markdown("---")
    st.subheader("What You Can Do")

    render(pd.DataFrame({
        "What": ["Online shopping (Amazon, anything)", "In-store NFC tap to pay", "ATM withdrawals", "Bank transfer to another account", "Pay contractors directly", "No 1099 from card", "Card requires EU/LatAm residency"],
        "How": ["Visa accepted anywhere", "Apple Pay / Google Pay", "Compatible ATMs worldwide", "Send from your wallet", "Send USDT to their wallet", "It's your wallet, not theirs", "True self-custody, but card has residency check"],
    }))

    st.markdown("---")
    st.subheader("vs Other Cards")

    render(pd.DataFrame({
        "Feature": ["Who holds your USDT?", "Can they freeze it?", "Do they have your ID on file?", "IRS reporting?", "Card requires"],
        "Bleap": ["Bleap company", "Yes", "Yes (gov ID + selfie)", "Yes", "Global (KYC upload)"],
        "RedotPay": ["RedotPay company", "Yes", "Yes (gov ID + selfie)", "Yes", "Global (KYC upload)"],
        "Gnosis Safe + Pay": ["YOU (self-custody)", "No — impossible", "No gov ID upload", "No 1099 from card", "EU/LatAm residency"],
    }))

    st.markdown("---")
    st.subheader("How to Set Up")

    steps = [
        ("1", "Download Gnosis Safe app", "safe.global or app store"),
        ("2", "Create a wallet", "Write down your seed phrase. Store it somewhere safe."),
        ("3", "Fund it with USDT", "Transfer USDT from wherever you have it"),
        ("4", "Connect to Gnosis Pay", "Inside the app, link your wallet and EU/LatAm bank account to Gnosis Pay"),
        ("5", "Get a virtual debit card", "Instant — works right away"),
        ("6", "Start spending / ATM withdrawals", "Tap to pay, online shopping, ATM"),
    ]
    for num, title, desc in steps:
        c1, c2 = st.columns([1, 5])
        c1.markdown(f"**{num}**")
        c2.markdown(f"**{title}** — {desc}")

    st.warning("Limitation: Gnosis Pay card requires EU or Latin American residency + a bank account in a supported country. NOT available in the US. You are NOT anonymous — your bank account identifies you. No passport upload needed, but the card issuer knows who you are through your bank.")

# ─── PAGE 5B: DEBIT CARDS ──────────────────────────────────────────────────
def page_cards():
    st.title("💳 Crypto Debit Cards — Full Comparison")
    st.subheader("Spend USDT anywhere Visa/Mastercard is accepted. ATM withdrawals. Compare all options.")
    st.markdown("---")

    st.success("""
**The two types:**

**Self-custody:** Your wallet, your money. No company holds it. (Gnosis Pay)
**Custodial:** The company holds your USDT and converts it when you spend. (Bleap, RedotPay)

**Both give you a physical or virtual card. Both work worldwide.**
""")

    st.markdown("---")
    st.subheader("All Cards Compared")

    render(pd.DataFrame({
        "Card": ["Gnosis Pay", "SolCard (KYC now)", "Bleap Mastercard", "RedotPay", "COCA Card", "Binance Card"],
        "Custody": ["YOU (self-custody)", "SolCard platform", "Bleap (custodial)", "RedotPay (custodial)", "COCA (custodial)", "Binance (custodial)"],
        "Network": ["Visa", "Visa", "Mastercard", "Visa", "Mastercard", "Visa"],
        "Cashback": ["Up to 5% (GNO tokens)", "None", "2% (USDC)", "3%", "Up to 5%", "Up to 5%"],
        "FX Fee": ["0.5% + 1% weekend", "0%", "0%", "0%", "0%", "0%"],
        "Monthly Fee": ["Free — €16.99 (Metal)", "Free", "Free", "Free", "Free", "Free"],
        "Top-Up Fee": ["None", "5% (virtual tier)", "None", "None", "None", "None"],
        "ATM Limit": ["Tiered by plan", "No ATM", "$400/mo free", "$100K/day", "Tiered", "Tiered"],
        "Spending Limit": ["$1M+/day (Metal)", "$5K/month", "High", "$1M/day", "High", "Medium"],
        "KYC": ["EU/LatAm residency + bank account", "Yes (removed no-KYC Apr 2026)", "Gov ID + selfie", "Gov ID + selfie", "Gov ID + selfie", "Gov ID + selfie"],
        "Countries": ["EU + LatAm (no US)", "Global", "Global", "Global", "Global", "Limited"],
        "Best For": ["Privacy first", "Crypto funded card", "Best overall fees", "High limits", "Multi-chain", "Binance users"],
    }))

    st.markdown("---")
    st.subheader("Gnosis Pay — Most Private (Self-Custody)")

    st.markdown("""
**What it is:** Visa debit card linked directly to your Gnosis Safe wallet. Your USDT never leaves your wallet. Card requires EU/LatAm residency AND a bank account in a supported country. No passport/selfie upload — but your bank account and residency effectively identify you.

**How it works:**
```
YOUR GNOSIS SAFE WALLET ($10M USDT)
        ↓
Gnosis Pay creates a virtual Visa card
        ↓
You buy something or withdraw from ATM
        ↓
Transaction settles from YOUR wallet
        ↓
YOU NEVER SOLD ANYTHING.
No company holds your money. No one can freeze it.
```

**Countries available:**
Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, Argentina, Brazil, Colombia.

**NOT available in the US yet.**
""")

    render(pd.DataFrame({
        "Tier": ["Standard (Free)", "Premium (€7.99/mo)", "Metal (€16.99/mo)"],
        "FX Fee": ["0.5% + 1% weekend markup", "Lower limits", "Higher limits"],
        "ATM": ["Tiered by plan", "Higher", "Highest"],
        "Cashback": ["Up to 4%", "Up to 4%", "Up to 5% (with GNO)"],
        "Notes": ["Free to start", "More free ATM", "Best limits + most cashback"],
    }))

    st.markdown("---")
    st.subheader("SolCard — No-KYC REMOVED (April 2026)")

    st.error("""
**SolCard removed its no-KYC feature in April 2026.** The anonymous virtual card that previously required no identity verification is gone. All tiers now require some form of KYC.

KYC is now required for all new cards. Existing no-KYC cards continue to work temporarily but will eventually require verification.

**This was the last no-KYC crypto debit card. As of May 2026, no crypto debit card exists without government ID.**
""")

    st.markdown("""
**What SolCard still offers (with KYC):**
- Visa debit card funded from self-custody wallet
- Physical and virtual cards available
- Apple Pay / Google Pay support
- Website: solcard.cc
""")

    st.markdown("---")
    st.subheader("Bleap Mastercard — Best Overall Fees")

    st.markdown("""
**What it is:** Mastercard issued by Bleap. Zero FX fees. Zero monthly fees. 2% cashback in USDC. Free ATM withdrawals up to $400/month worldwide.

**The numbers:**
- Monthly fee: $0
- FX fee: 0% (zero foreign transaction fees)
- Cashback: 2% in USDC, auto-credited
- ATM withdrawals: Free up to $400/month worldwide. Above that: only the ATM operator's fee.
- Spending limit: High (verified users)
- KYC: Government ID + selfie required

**Why it's good:** Cheapest card for everyday spending. No FX markup. No monthly fee. 2% cashback adds up fast.

**Countries:** Global (UK, Switzerland, EU, and more)
""")

    st.markdown("---")
    st.subheader("RedotPay — Highest Limits")

    st.markdown("""
**What it is:** Visa card with massive limits. $100K per transaction. $1M daily spending. $200K monthly ATM withdrawals.

**The numbers:**
- Monthly fee: $0
- FX fee: 0% (promoted as key feature)
- Cashback: 3% (in their token or stablecoins)
- ATM: $100,000/day per transaction
- Monthly spending: $1,000,000
- Monthly ATM: $200,000
- KYC: Government ID + selfie required

**Why it's good:** If you need to move serious money through a card, this is the one. Visa BIN means it works on Google Ads and Meta Ads.

**Countries:** Global
""")

    st.markdown("---")
    st.subheader("COCA Card — Multi-Chain")

    st.markdown("""
**What it is:** Mastercard via Wirex. No joining or monthly fees. Supports multiple stablecoins and chains.

**The numbers:**
- Monthly fee: $0
- FX fee: 0%
- Cashback: Up to 5% on certain spending
- ATM: Tiered by account level
- KYC: Government ID required

**Why it's different:** Works across multiple chains and stablecoins. Good if you hold different assets.
""")

    st.markdown("---")
    st.subheader("The Privacy Comparison")

    render(pd.DataFrame({
        "Card": ["Gnosis Pay", "Bleap", "RedotPay", "COCA"],
        "Who Holds Your USDT": ["YOU", "Bleap company", "RedotPay company", "COCA"],
        "Can They Freeze It": ["No — impossible", "Yes", "Yes", "Yes"],
        "Do They Have Your ID": ["Residency check (EU/LatAm)", "Yes (gov ID)", "Yes (gov ID)", "Yes (gov ID)"],
        "IRS Knows About You": ["No 1099 from card", "Yes (1099)", "Yes", "Yes"],
        "Privacy Score": ["9/10", "4/10", "4/10", "4/10"],
    }))

    st.markdown("---")
    st.subheader("Which Card When")

    render(pd.DataFrame({
        "Situation": ["Most private — self-custody (EU/LatAm only)", "Best for everyday spending (low fees)", "Need to spend $100K+ through a card", "Already use Binance ecosystem", "Need card that works on Meta/Google Ads"],
        "Best Card": ["Gnosis Pay", "Bleap Mastercard", "RedotPay", "Binance Card", "RedotPay (US Visa BIN)"],
    }))

    st.error("""
**No crypto debit card exists without KYC in 2026.** SolCard removed its no-KYC feature April 2026. All remaining cards (Bleap, RedotPay, COCA, Binance) require government ID + selfie. Gnosis Pay does not require ID because your Safe IS the account — but it is only available in EU + Latin America.

**The path to a bank debit card with no crypto label:** USDT → swap to BTC → collateral loan → wire to bank → request bank debit card from your bank.
""")

# ─── PAGE 6: DEX + OFF-RAMP ─────────────────────────────────────────────────
def page_dex():
    st.title("💱 DEX → Off-Ramp — No-KYC Path to Cash")
    st.subheader("Swap USDT to USDC. Off-ramp to cash. No ID at any step.")
    st.markdown("---")

    st.success("""
**The model:**
- Deposit USDT into a DeFi protocol (no ID)
- Borrow USDC (no ID, instant)
- Send USDC to a no-KYC exchange
- They wire or send cash to you

**No crypto company knows who you are. Bank sees a wire from a payment processor.**
""")

    st.markdown("---")
    st.subheader("The Path")

    st.code("""
USDT
  ↓ Aave V3 / Morpho Blue / Spark / Compound (no ID)
Borrow USDC
  ↓ SimpleSwap / Godex / AceChange / Exolix (no ID)
USDC → USD via swap or P2P
  ↓
Wire to your bank — OR —
Cash in your hand
""", language=None)

    st.markdown("---")
    st.subheader("Step by Step")

    steps = [
        ("1", "Open MetaMask or Trust Wallet", "Fund it with your USDT"),
        ("2", "Go to Aave V3", "app.aave.com — deposit USDT, borrow USDC"),
        ("3", "Borrow USDC", "No ID. Instant. Just pay the interest."),
        ("4", "Send USDC to SimpleSwap", "simpleswap.io — no account needed"),
        ("5", "Swap USDC to USD", "Choose: wire to bank, cash pickup, or P2P"),
        ("6", "Get cash or wire", "Done. Bank sees: wire from SimpleSwap."),
    ]
    for num, title, desc in steps:
        c1, c2 = st.columns([1, 5])
        c1.markdown(f"**{num}**")
        c2.markdown(f"**{title}** — {desc}")

    st.markdown("---")
    st.subheader("No-KYC Off-Ramps")

    render(pd.DataFrame({
        "Platform": ["SimpleSwap", "Godex", "AceChange", "Exolix", "StealthEX", "ChangeNOW"],
        "KYC": ["None (may flag)", "None (no account)", "None (no registration)", "None", "None", "None (<$1.5K)"],
        "Output": ["Wire, cash, crypto", "Wire, crypto", "Wire, crypto", "Wire, cash, crypto", "Wire, crypto", "Wire, crypto"],
        "Speed": ["Hours", "Fast", "Fast", "Fast", "Fast", "Fast"],
        "Coins": ["300+", "200+", "100+", "200+", "800+", "200+"],
        "Notes": ["Best overall", "Built no-KYC from ground up", "Specialized non-KYC", "Fast, no account", "Non-custodial", "<$1.5K no ID"],
    }))

    st.markdown("---")
    st.subheader("What the Bank Sees")

    st.markdown("""
**Normal wire from SimpleSwap.**

Bank sees: payment processor wire
Bank does NOT see: crypto, USDT, blockchain, or any of your wallets

**This is the cleanest privacy route.**
""")

    st.markdown("---")
    st.warning("More DeFi options: Spark Protocol (Aave fork, USDS lending), Compound III (single-collateral pools), Venus Protocol (BNB Chain, $3.7M exploit Mar 2026). Use Morpho Blue for better ETH rates. Always test with a small amount first.")

# ─── PAGE 7: PRIVACY ─────────────────────────────────────────────────────────
def page_privacy():
    st.title("🛡️ Privacy Stack — Ranked")
    st.subheader("Most private → Least private. No government ID where possible.")
    st.markdown("---")

    render(pd.DataFrame({
        "Rank": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "Method": ["Local meet (in person)", "Goods arbitrage", "Gnosis Safe + Pay", "P2P platform", "Gift cards to resell", "Travel to resell", "DEX to off-ramp", "Loan (debt)"],
        "ID Needed": ["None", "None", "None", "None", "Email only", "No (<$3K)", "None", "Yes (loan company)"],
        "Scale": ["Small", "Large", "Large", "Unlimited", "Large", "Medium", "Large", "Large"],
        "Risk": ["Trust-based", "None", "None", "AML watch at scale", "Gift card resale", "Booking resale", "None", "Credit report"],
    }))

    st.markdown("---")
    st.subheader("The Rules")

    rules = [
        ("Cash is king", "Physical cash is untraceable. In-person trades are the most private."),
        ("Your wallet, your rules", "Gnosis Safe = no company holds your money. No one can freeze it."),
        ("Debt is invisible", "A loan shows on your credit report but the bank has no idea it's crypto-backed."),
        ("Under $10K cash", "Bank SARs trigger at $10,000+ in one cash deposit. Keep trades smaller."),
        ("One wallet per purpose", "Don't mix wallets. Fresh wallet for large transfers."),
        ("On-chain transfers", "Keep large transfers under $1,000 or use fresh wallets."),
    ]
    for title, desc in rules:
        st.markdown(f"**{title}:** {desc}")

    st.markdown("---")
    st.subheader("What Triggers Attention")

    render(pd.DataFrame({
        "Thing": ["$10K+ cash deposit", "Large P2P volume at scale", "New bank account receiving wire", "Structuring (splitting deposits)"],
        "What Happens": ["Bank files SAR automatically", "Platform monitors for AML", "Bank may ask questions", "Looks like hiding — felony"],
        "How to Avoid": ["Keep trades under $10K", "Get FinCEN MSB + MTL", "Use an existing account", "Deposit larger amounts or use wire"],
    }))

# ─── PAGE 8: BANKING ──────────────────────────────────────────────────────────
def page_banking():
    st.title("🏦 Banking — Where to Put the Cash")
    st.subheader("Options from US banks to offshore. Which one fits your situation.")
    st.markdown("---")

    st.success("""
**The key insight:** Banks see DEBT, not the collateral.

A wire from Ledn = "personal loan." Banks see thousands of these per day.
A wire from Panama = normal USD from abroad. Completely normal in dollarized countries.
A wire from FV Bank = a US bank. Not a crypto company.

**The source of the wire matters less than you think.**
""")

    st.markdown("---")
    st.subheader("US Banks — Loan Route")

    render(pd.DataFrame({
        "Bank": ["FV Bank (Puerto Rico)", "Cross River Bank", "Ledn wire to your existing bank"],
        "What It Is": ["US bank, accepts USDC directly", "Tech bank behind Coinbase", "Wire from Ledn to your account"],
        "KYC": ["Yes", "Yes", "Yes (at Ledn only)"],
        "Output": ["USD wire, USDC deposit", "Corporate accounts, wire transfers", "USD wire"],
        "Best For": ["Direct stablecoin bridge", "Crypto businesses", "Simplest US option"],
    }))

    st.markdown("---")
    st.subheader("Offshore — Dollarized Countries")

    st.markdown("""
**Best for:** USD wires are completely normal. Banks don't bat an eye.

**Panama** ⭐ — Dollarized. USD is the currency. Large USD wires are routine.
**UAE / Dubai** — Growing crypto hub. No income tax.
**Cayman Islands** — Corporate accounts. Major money jurisdiction.
**Hong Kong** — USD-pegged. Major financial center.
""")

    render(pd.DataFrame({
        "Country": ["Panama", "UAE / Dubai", "Cayman Islands", "Hong Kong"],
        "Currency": ["USD", ["USD", "AED"], "USD", "USD / HKD"],
        "Tax": ["None on foreign income", "None", "None", "Low"],
        "Crypto Friendly": ["Some banks", "Growing", "Yes (corporate)", "Some banks"],
        "What You Need": ["Residency or company", "Residency or company", "Company setup", "Company or residency"],
        "KYC": ["Basic", "Basic to moderate", "Moderate", "Moderate"],
    }))

    st.markdown("---")
    st.subheader("Foreign Bank Flow")

    st.code("""
USDT
  ↓
Swap to BTC/ETH (one taxable event)
  ↓
Use BTC as collateral at loan platform
  ↓
They wire USD to your foreign bank (Panama / UAE / etc.)
  ↓
Foreign bank sees: USD wire, debt on the books
No US IRS reporting. No US questions.
""", language=None)

    st.markdown("---")
    st.subheader("Banks That Actually Work")

    render(pd.DataFrame({
        "Bank": ["BAC (Panama)", "Global Bank (Panama)", "Cross River (US)", "FV Bank (Puerto Rico)"],
        "Type": ["Offshore USD", "Offshore USD", "US Tech Bank", "US Digital Bank"],
        "Crypto Wire": ["Yes", "Yes", "Yes", "Yes (USDC direct)"],
        "KYC": ["Yes", "Yes", "Yes", "Yes"],
        "Notes": ["No questions on USD wires", "USD normal there", "Works with fintech partners", "Only US bank with USDC deposit"],
    }))

    st.warning("Mercury Bank is closed (2024). Big US banks (Chase, BofA) block crypto exchanges inconsistently. Not reliable.")

# ─── PAGE 9: FRAUD CASES ────────────────────────────────────────────────────
def page_fraud():
    st.title("⚠️ How They Got Caught")
    st.subheader("Real cases. Learn what NOT to do.")
    st.markdown("---")

    cases = [
        ("Crypto Dispensers — Nov 2025", "$10M+ alleged money laundering", "Ran cash-to-BTC ATMs. Banks flagged cash deposits. FBI traced through ATMs. Company exploring $100M sale during prosecution.", "Cash deposits trigger SARs. Every ATM transaction is on-chain."),
        ("Paxful — Nov 2025", "$3.5M-4M fine + shut down", "No MTL licenses. No KYC/AML. Platform used by scammers. Shut down Nov 1 2025.", "Get licensed before doing serious volume."),
        ("Samourai Wallet — 2025", "Co-founders: 48 months prison", "Privacy mixing wallet. Explicit money laundering intent. Both co-founders sentenced.", "Privacy tools treated as intent to hide money."),
        ("Ronald Spektor — Dec 2025", "$16M fraud, Brooklyn DA", "Impersonated Coinbase support. 31 counts including grand larceny. 23 years old.", "Scamming = prison."),
        ("Tether Freezes — 2025-2026", "$344M+ frozen (documented)", "Tether froze USDT connected to fraud. DOJ froze $344M in one action (2026).", "Tether can freeze your USDT instantly on DOJ request."),
        ("Operation Atlantic — May 2026", "276 arrests, millions seized", "US + China + Dubai coordinated crackdown on pig-butchering scam centers.", "International law enforcement is highly coordinated."),
    ]

    for name, amount, what, lesson in cases:
        with st.expander(f"{name} — {amount}"):
            st.markdown(f"**What happened:** {what}")
            st.error(f"**Lesson:** {lesson}")

    st.markdown("---")
    st.subheader("How They All Got Caught")

    render(pd.DataFrame({
        "Method": ["Blockchain tracing", "Bank SAR filings", "Exchange subpoenas", "Tether freezing", "Victim reports to FBI"],
        "What It Is": ["Chainalysis/TRM trace wallet history", "Bank reports suspicious activity to FinCEN", "Government subpoena → exchange gives up KYC", "Tether freezes on DOJ/OFAC request", "FBI IC3 complaints start investigations"],
    }))

    st.markdown("---")
    st.subheader("How to NOT Be Them")

    render(pd.DataFrame({
        "Do": ["Get FinCEN MSB if doing serious volume", "Basic KYC on platform users at scale", "File SARs when something looks wrong", "Keep records of all trades"],
        "Don't": ["Run P2P at scale without MTL", "Ignore red flag transactions", "Use privacy mixers or tumblers", "Skip compliance entirely"],
    }))

    st.error("At $10M in volume, you are visible. Get some basic compliance. It's not that hard and it keeps you free.")

# ─── PAGE 10: APPS ───────────────────────────────────────────────────────────
def page_apps():
    st.title("📱 The Apps — All in One Place")
    st.subheader("What to download. What to use. No government ID where possible.")
    st.markdown("---")

    st.subheader("Private First (No ID)")

    render(pd.DataFrame({
        "App": ["Gnosis Safe", "CoinGate", "MetaMask", "Trust Wallet", "Travala", "Telegram", "SimpleSwap", "Exolix"],
        "What It's For": ["Self-custody wallet + card (EU/LatAm, bank required)", "Gift cards with email only", "DEX swaps", "Backup wallet", "Flights + hotels with USDT", "P2P matching", "No-KYC USDC to wire/cash", "No-KYC USDC to wire/cash"],
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
        "What It's For": ["Spend USDT anywhere, debit card", "High limits, US Visa BIN", "P2P platform", "Decentralized P2P, escrow built-in"],
        "ID Needed": ["Gov ID + selfie", "Gov ID + selfie", "Account needed", "Account needed"],
        "Website": ["bleap.finance", "redotpay.com", "noones.com", "localcoinswap.com"],
    }))

    st.markdown("---")
    st.subheader("The Daily Stack")

    st.markdown("---")
    st.subheader("The Reality Check")

    st.warning("""
**No wallet-to-card shortcut exists in 2026.** You cannot go USDT wallet → debit card directly without KYC. Every card issuer (Visa, Mastercard) requires identity verification by law. SolCard was the last no-KYC option and they removed it April 2026.

**The only path to a bank debit card:** USDT → swap to BTC → collateral at Ledn/Unchained → wire to bank → bank debit card.

**OR use the cash methods:** P2P, gift cards, goods arbitrage, Gnosis Safe spending.
""")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        **Morning:**
        - Check Telegram P2P groups
        - Match 5-10 trades
        - Confirm cash received
        - Release USDT
        """)
    with c2:
        st.markdown("""
        **Afternoon:**
        - Buy gift cards on CoinGate
        - Post for sale
        - Collect cash
        """)
    with c3:
        st.markdown("""
        **Ongoing:**
        - Gnosis Safe for spending / ATM
        - Build repeat relationships
        - Scale P2P volume
        - Track all trades
        """)

# ─── PAGE 11: SHORTCUTS ─────────────────────────────────────────────────────
# ─── PAGE 6B: BUSINESS SPENDING ─────────────────────────────────────────────
def page_business():
    st.title("🏢 Business Spending — Use USDT Without Converting")
    st.subheader("Pay expenses directly with USDT. No need to convert to cash first.")
    st.markdown("---")

    st.success("""
**The idea:** Instead of converting USDT to cash and THEN spending it — just spend the USDT directly on real things.

If you can pay for things in USDT, you never need to convert it. No conversion = no tax event = no bank involvement.
""")

    st.markdown("---")
    st.subheader("Real Estate — RealOpen")

    st.markdown("""
**RealOpen.com** — Buy property worldwide with USDT. No conversion needed.

- $9.4 million in USDT verified for U.S. crypto home purchases (April 2026)
- No withdrawal limits. No friction.
- Buy homes with Bitcoin, Ethereum, or any major crypto
- Works like a normal real estate transaction — title transfer, escrow, everything
- Properties worldwide
""")

    st.markdown("---")
    st.subheader("Gold — SuisseGold")

    st.markdown("""
**SuisseGold.com** — Buy physical gold and silver with USDT.

- Accepts Tether (USDT) payments directly (launched March 2026)
- Physical gold and silver delivered
- Crypto-to-bullion direct
- No need to convert to fiat first

**Why gold:** Different asset class. Holds value. If you want to diversify — gold is the classic answer.
""")

    st.markdown("---")
    st.subheader("Payroll — Bitwage")

    st.markdown("""
**Bitwage.com** — Send payroll or receive salary in USDT. $400M+ processed.

- 11 years in business. Now part of Paystand.
- Integrates with ADP and Gusto
- No fees on crypto payouts
- No custody issues — goes directly to your wallet

**How to use it:**
- Pay contractors and freelancers in USDT
- Receive your own salary in USDT
- No bank needed on the receiving end
""")

    st.markdown("---")
    st.subheader("Build a USDT-Native Business")

    st.markdown("""
**The model:**
1. Set up a business that accepts USDT payments
2. Pay all expenses in USDT where possible
3. Pay yourself a salary in USDT via Bitwage
4. Use RealOpen to buy property
5. Buy gold with SuisseGold

**You never convert USDT to fiat. You just spend it directly.**

**Companies that accept USDT directly:**
- Namecheap — domains, hosting
- Surfshark — VPN service
- Travala — travel for your team
- Many SaaS tools via crypto payment gateways (CoinGate, BitPay)
""")
def page_shortcuts():
    st.title("⚡ Shortcuts — Fastest Paths to Cash")
    st.subheader("Pick your situation. Get the fastest route. No fluff.")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["Cash Now (Today)", "Cash This Week", "Cash This Month"])


    with tab1:
        st.markdown("**If you need cash RIGHT NOW — same day:**")

        render(pd.DataFrame({
            "How": ["Local meet", "Gift cards", "Gnosis Pay ATM"],
            "What to Do": ["Telegram + local meet. Cash in hand.", "CoinGate: buy Steam cards. Sell for 85 cents on dollar.", "Gnosis Safe: ATM withdrawal (EU/LatAm)."],
            "Amount": ["Any size", "Up to $50K/day", "Per ATM limit"],
            "ID Needed": ["None", "Email only", "None"],
            "Risk": ["Trust-based", "Low", "None"],
        }))

        st.markdown("---")
        st.markdown("""
        **Fastest same-day path (no ID):**

        1. Go to CoinGate.com
        2. Buy Steam cards with USDT
        3. Post on CardTrader.com or Telegram
        4. Sell for 85 cents on the dollar
        5. Cash in your pocket same day

        **No ID. No bank. Cash in your pocket.**
        """)

    with tab2:
        st.markdown("**If you have a few days — more volume:**")

        render(pd.DataFrame({
            "How": ["P2P platform", "Goods arbitrage", "DEX to SimpleSwap"],
            "What to Do": ["LocalCoinSwap or NoOnes. Post ads. Match buyers and sellers.", "Buy and flip: cars, watches, electronics.", "Aave to USDC to SimpleSwap to wire or cash."],
            "Amount": ["Unlimited", "$10K to $1M+", "Up to DeFi liquidity"],
            "ID Needed": ["None", "None", "None"],
            "Time": ["1-3 days to get going", "3-7 days per flip", "1-3 days"],
        }))

        st.markdown("---")
        st.markdown("""
        **Best path this week:**

        1. Open MetaMask + fund with USDT
        2. Go to Aave V3 (app.aave.com)
        3. Deposit USDT, borrow USDC
        4. Send USDC to SimpleSwap.io
        5. Choose: wire to bank OR cash pickup

        **Bank sees: wire from SimpleSwap. No ID. Done in 3 days.**
        """)

    with tab3:
        st.markdown("**If you have a week or more — large amounts:**")

        render(pd.DataFrame({
            "How": ["Loan (debt)", "P2P platform at scale", "Real estate + resell"],
            "What to Do": ["Swap USDT to BTC, collateral at Ledn, wire to bank.", "Build Telegram presence + LocalCoinSwap + NoOnes.", "Buy property with USDT (RealOpen), resell for cash."],
            "Amount": ["Up to 50% of your USDT", "$100K to $10M+", "Large"],
            "ID Needed": ["Yes (at Ledn)", "None", "None (at RealOpen <$10K)"],
            "Time": ["1-2 weeks to setup", "1-4 weeks to build", "Weeks to months"],
        }))

        st.markdown("---")
        st.markdown("""
        **Best path for large amounts:**

        1. Swap USDT to BTC (one taxable event)
        2. Put BTC as collateral at Ledn.io
        3. They wire USD to your bank
        4. Bank sees: personal loan from Ledn Capital
        5. Done. Clean entry to banking system.
        """)

    st.markdown("---")
    st.subheader("The Four-Fastest Methods — Ranked")

    render(pd.DataFrame({
        "Rank": ["1", "2", "3", "4"],
        "Method": ["Local meet (in person)", "Gift cards to CoinGate to resell", "Gnosis Safe + Pay (ATM)", "Aave to SimpleSwap (wire)"],
        "Speed": ["Instant", "Same day", "Instant", "1-3 days"],
        "ID Needed": ["None", "Email only", "None", "None"],
        "Bank Needed": ["No", "No", "No", "No"],
        "Amount": ["Any size", "Up to $50K/day", "Per ATM limit", "Large amounts"],
        "Privacy": ["Highest", "High", "Highest", "High"],
    }))

    st.markdown("---")
    st.subheader("Pick One and Start")

    st.markdown("""
    **Start here:**
    1. Download Gnosis Safe + CoinGate + Telegram
    2. Do one local meet this week
    3. Sell a gift card today
    4. Scale from there
    """)

# ─── APP SHELL ────────────────────────────────────────────────────────────────
PAGES = {
    "🏠 Home": page_home,
    "🤝 P2P": page_p2p,
    "💳 Loan": page_loans,
    "💵 Goods Arbitrage": page_goods,
    "🔐 Gnosis Safe": page_safe,
    "💳 Debit Cards": page_cards,
    "🏢 Business Spending": page_business,
    "💱 DEX + Off-Ramp": page_dex,
    "🛡️ Privacy": page_privacy,
    "🏦 Banking": page_banking,
    "⚠️ Fraud Cases": page_fraud,
    "📱 All Apps": page_apps,
    "⚡ Shortcuts": page_shortcuts,
}

st.sidebar.title("💸 USDT → Cash")
st.sidebar.caption("No government ID. No bank needed.")

selection = st.sidebar.radio("Navigate", list(PAGES.keys()), label_visibility="collapsed")
PAGES[selection]()