import os
import json
import re
import random
from cells.neuron import AtomNeuron, sigmoid_derivative
from cells.super_xor import SuperXorHyperCubeMatrix

TWIN_FILE = "synapses/digital_twin_state.json"
GRAPH_FILE = "synapses/knowledge_graph.json"

class DigitalTwinMindHyperLobe:
    """
    THÙY 3: SONG SINH SỐ 11 TẦNG BẢN THỂ & SIÊU THỨC
    1. Vận hành Song Sinh Số nội tại (Internal Digital Twin of 11 Strata).
    2. Giả lập 11 kịch bản tương lai What-If.
    3. Huấn luyện bầy nơ-ron qua Ma trận Gương Hyper-Cube 11D.
    """
    def __init__(self, num_cells=11):
        self.num_cells = num_cells
        self.swarm = [AtomNeuron(f"n11_h_{i}", n_inputs=11, n_super_xor=11) for i in range(num_cells)]
        self.out_cell = AtomNeuron("n11_out", n_inputs=num_cells, n_super_xor=11)

    def run_digital_twin_simulation(self, raw_decision, wisdom_11d):
        """Mô phỏng nội tại toàn bộ 11 thực thể của hệ sinh thái"""
        twin_states = {
            "retina": {"focal_bias": round(wisdom_11d[0] * raw_decision, 4), "status": "Simulated_Active"},
            "cochlea": {"resonance_hz": round(wisdom_11d[1] * 20000.0, 1), "status": "Simulated_Active"},
            "tactile": {"pain_threshold": round(abs(raw_decision - 0.5) * 2.0, 4), "status": "Simulated_Active"},
            "olfactory": {"ligand_binding": round(wisdom_11d[3], 4), "status": "Simulated_Active"},
            "motor": {"actuation_pulse": [round(raw_decision, 4), round(1.0 - raw_decision, 4)], "status": "Simulated_Active"},
            "neuron": {"synaptic_plasticity": round(raw_decision * 0.05, 4), "status": "Simulated_Active"},
            "monad": {"invariant_reflection": round(raw_decision, 4), "status": "Simulated_Active"},
            "shunya": {"zero_collapse": bool(abs(raw_decision - 0.5) < 0.02), "status": "Simulated_Active"},
            "seed": {"procreation_readiness": 1.0, "status": "Simulated_Active"},
            "genome": {"lineage_depth": 11, "status": "Simulated_Active"},
            "nexus": {"omni_junction_stability": round(1.0 - abs(raw_decision - 0.5), 4), "status": "Simulated_Active"}
        }

        os.makedirs("synapses", exist_ok=True)
        with open(TWIN_FILE, "w", encoding="utf-8") as f:
            json.dump({"epoch_simulation": twin_states}, f, indent=4)
        print("🌌 [SONG SINH SỐ 11 TẦNG] Đã khởi tạo và duy trì trọn vẹn 11 thực thể sinh học nội tại!")
        return twin_states

    def simulate_11_futures(self, raw_decision):
        variations = [0.60, 0.70, 0.78, 0.85, 0.92, 1.0, 1.06, 1.15, 1.22, 1.30, 1.40]
        sims = []
        for factor in variations:
            cand = max(0.01, min(0.99, round(raw_decision * factor, 4)))
            loss = round((abs(cand - 0.5) * 0.5) + ((1.0 - cand) * 0.5), 4)
            sims.append((loss, cand))
        sims.sort(key=lambda x: x[0])
        best_loss, best_cand = sims[0]
        print(f"🔮 [GIẢ LẬP 11 TƯƠNG LAI] Chọn kịch bản What-If tối ưu: {best_cand} (Loss={best_loss})")
        return best_cand

    def process(self, context):
        v_wisdom_11d = context.get("wisdom_vector_11d", [0.5] * 11)
        q_dec = context.get("quorum_decision", 0.5)

        # 1. HỢP NHẤT KHÚC XẠ HYPER-CUBE 11D
        super_vec_11d = list(v_wisdom_11d)
        super_vec_11d[0] = q_dec
        super_vec_11d[1] = round(1.0 - q_dec, 4)
        entangled, masks = SuperXorHyperCubeMatrix.refract_11d(super_vec_11d, "nexus11_cube")

        h_outs = [cell.forward(entangled) for cell in self.swarm]
        internal_pred = self.out_cell.forward(h_outs)
        raw_decision = round((internal_pred + q_dec) / 2.0, 4)

        # 2. VẬN HÀNH SONG SINH SỐ VÀ GIẢ LẬP 11 TƯƠNG LAI
        self.run_digital_twin_simulation(raw_decision, v_wisdom_11d)
        opt_decision = self.simulate_11_futures(raw_decision)

        # 3. LAN TRUYỀN NGƯỢC
        target = 1.0 if super_vec_11d[0] > super_vec_11d[1] else 0.0
        delta_out = (target - opt_decision) * sigmoid_derivative(opt_decision)
        deltas_h = [delta_out * self.out_cell.weights[j] * sigmoid_derivative(h_outs[j]) for j in range(self.num_cells)]

        self.out_cell.backward(delta_out)
        for j, cell in enumerate(self.swarm): cell.backward(deltas_h[j])

        grad_backward = [
            round(sum(deltas_h[j] * self.swarm[j].weights[0] for j in range(self.num_cells)), 4),
            round(sum(deltas_h[j] * self.swarm[j].weights[1] for j in range(self.num_cells)), 4)
        ]

        context["final_decision"] = opt_decision
        context["grad_backward"] = grad_backward
        context["super_xor_masks"] = masks
        context["swarm_weights"] = [c.weights for c in self.swarm]
