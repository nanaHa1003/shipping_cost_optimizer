from flask import Flask, render_template, request, jsonify
from logic import Item, ShippingOptimizer
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app, content_security_policy=None) # 強制 HTTPS 並加入安全標頭

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    # 獲取前端傳來的自定義配置
    cfg = data.get("config", {})
    opt = ShippingOptimizer(
        first_kg_cost=float(cfg.get("first_kg", 137)),
        next_kg_cost=float(cfg.get("next_kg", 112)),
        surcharge_threshold=int(cfg.get("threshold", 8)),
        surcharge_fee=float(cfg.get("surcharge", 5))
    )
    
    items = [Item(i["name"], i["weight"], i["tracking_no"]) for i in data["items"]]
    optimized_total, result_parcels, all_in_one_cost = opt.solve(items)
    
    response = {
        "optimized_total": optimized_total,
        "all_in_one_cost": all_in_one_cost,
        "savings": all_in_one_cost - optimized_total,
        "parcels": []
    }

    for p in result_parcels:
        total, base, sur = opt.calculate_detailed_cost(p)
        response["parcels"].append({
            "items": [{"name": it.name, "tracking": it.tracking_no} for it in p],
            "weight": sum(it.weight for it in p),
            "base_cost": base,
            "surcharge": sur,
            "total": total
        })
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
