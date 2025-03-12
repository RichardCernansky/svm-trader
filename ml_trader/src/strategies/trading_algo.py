def long_only_trading(df, svm_model, gamma=0.1, sG=0.05, sL=0.05, initial_cash=1000):
    cash = initial_cash
    bitcoins = 0
    portfolio_value = cash
    values = []

    for t in range(len(df) - 1):
        X_t = scaler.transform(df.iloc[t][features].values.reshape(1, -1))
        pred_class = svm_model.predict(X_t)[0]
        pred_prob = svm_model.predict_proba(X_t)[0]
        margin = abs(pred_prob.max() - pred_prob.min())  # Signed distance margin

        Pt = df.iloc[t]["Close"]

        # If holding cash and strong buy signal
        if cash > 0 and pred_class == 1 and margin >= gamma:
            bitcoins = cash / Pt
            cash = 0
            portfolio_value = bitcoins * Pt

        # If holding bitcoin and strong sell signal
        elif bitcoins > 0 and pred_class == -1 and margin >= gamma:
            cash = bitcoins * Pt
            bitcoins = 0
            portfolio_value = cash

        # Take-profit or stop-loss condition
        elif bitcoins > 0:
            P_t1 = df.iloc[t + 1]["Close"]
            profit_loss = (bitcoins * P_t1 - portfolio_value) / portfolio_value

            if profit_loss >= sG or profit_loss <= -sL:
                cash = bitcoins * P_t1
                bitcoins = 0
                portfolio_value = cash

        values.append(portfolio_value)

    return values
