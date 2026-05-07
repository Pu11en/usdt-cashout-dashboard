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
**The goal:** USDT in your wallet. Cash in your pocket. No government ID. No bank account. No one keeping a file on you.

**How it works:**
- P2P: Connect cash people to USDT people. Take the spread.
- DeFi lending: Deposit USDT, borrow USDC, off-ramp to cash. No ID.
- Goods arbitrage: Buy things with USDT, sell them for cash.

**All private. No bank needed.**
""")

    st.markdown("---")
    st.subheader("All Ways to Get USDT → Cash")

    render(pd.DataFrame({
        "Method": [
            "🤝 P2P — Cash people want USDT (in person or platform)",
            "💵 Goods arbitrage — Buy with USDT, sell for cash",
            "🎁 Gift cards — Buy with USDT, sell for cash",
            "✈️ Travel — Buy bookings, resell",
            "💳 DeFi Loan — USDT as collateral, borrow USDC",
            "💱 DEX Off-ramp — Swap, wire, cash",
        ],
        "Output": [
            "Cash via escrow or in person",
            "Cash from reselling",
            "Cash from reselling",
            "Cash from reselling",
            "USDC or cash",
            "Wire or cash",
        ],
        "ID Needed": [
            "None",
            "None",
            "Email only",
            "No (<$3K)",
            "No ID (DeFi)",
            "No ID (off-ramp)",
        ],
        "Best For": [
            "Main business — scale up",
            "Large items",
            "Quick turnaround",
            "People who need travel",
            "Large amounts, private",
            "Privacy route to cash",
        ],
    }))

    st.markdown("---")
    st.subheader("The Three Angles")

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
        **3. DeFi Lending**
        Deposit USDT into DeFi.
        Borrow USDC. Off-ramp to cash.
        No ID. No bank. No questions.
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
    st.subheader("DeFi lending. No bank. No ID. Get USDC. Off-ramp to cash.")
    st.markdown("---")

    st.success("""
**The key insight:** DeFi lending requires no ID. Deposit USDT into Aave V3 or Morpho Blue. Borrow USDC. Off-ramp to cash via SimpleSwap or Godex.

No company knows who you are. No bank account needed. No tax event until you swap back to fiat.

**This is the most private lending path in crypto.**
""")

    st.markdown("---")
    st.subheader("No-Bank Route (Cash Only)")

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
    st.warning("USDT is accepted as collateral on Aave V3, Morpho Blue, Spark, and Compound. Borrow USDC. Send to SimpleSwap, Godex, or AceChange. Off-ramp to cash. No ID at any step.")

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
        "Rank": ["1", "2", "3", "4", "5", "6"],
        "Method": ["P2P (in person or platform)", "Goods arbitrage", "DeFi lending + off-ramp", "Gift cards to resell", "Travel to resell", "DEX to SimpleSwap"],
        "ID Needed": ["None", "None", "No ID", "Email only", "No (<$3K)", "No ID"],
        "Scale": ["Unlimited", "Large", "Large", "Large", "Medium", "Large"],
        "Risk": ["AML watch at scale", "None", "No counter-party", "Gift card resale", "Booking resale", "Exchange KYC flag"],
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
def page_shortcuts():
    st.title("⚡ Shortcuts — Fastest Paths to Cash")
    st.subheader("Pick your situation. Get the fastest route. No fluff.")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["Cash Now (Today)", "Cash This Week", "Cash This Month"])


    with tab1:
        st.markdown("**If you need cash RIGHT NOW — same day:**")

        render(pd.DataFrame({
            "How": ["P2P (in person)", "Gift cards", "Gnosis Pay ATM"],
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
        "Method": ["P2P (in person or platform)", "Gift cards via CoinGate", "Gnosis Safe + Pay (ATM)", "Aave to SimpleSwap (wire)"],
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
    2. Do one P2P trade this week
    3. Sell a gift card today
    4. Scale from there
    """)

# ─── APP SHELL ────────────────────────────────────────────────────────────────
PAGES = {
    "🏠 Home": page_home,
    "🤝 P2P": page_p2p,
    "💳 Loan": page_loans,
    "💵 Goods Arbitrage": page_goods,
    "💱 DEX + Off-Ramp": page_dex,
    "🛡️ Privacy": page_privacy,
    "⚠️ Fraud Cases": page_fraud,
    "📱 All Apps": page_apps,
    "⚡ Shortcuts": page_shortcuts,
}

st.sidebar.title("💸 USDT → Cash")
st.sidebar.caption("No government ID. No bank needed.")

selection = st.sidebar.radio("Navigate", list(PAGES.keys()), label_visibility="collapsed")
PAGES[selection]()