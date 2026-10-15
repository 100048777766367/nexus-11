import os
import json
import time
import hashlib
import subprocess

RELIQUARY_FILE = "synapses/ancestral_reliquary.json"
HONORS_FILE = "synapses/honors_registry.json"
SOULS_FILE = "synapses/reincarnated_souls.json"
COMPASS_FILE = "synapses/teleology_compass.json"
CAPSULE_FILE = "synapses/seed_capsule_f12.json"
AVATAR_PROXY_DIR = "synapses/avatar_proxies"

BHUMI_11D = [
    "Pramudita (Hoan Hỷ)", "Vimala (Ly Cấu)", "Prabhakari (Phát Quang)",
    "Arcismati (Diễm Huệ)", "Sudurjaya (Nan Thắng)", "Abhimukhi (Hiện Tiền)",
    "Durangama (Viễn Hành)", "Acala (Bất Động)", "Sadhumati (Thiện Huệ)",
    "Dharmamegha (Pháp Vân)", "Prabhasvara (Phổ Quang Viên Mãn)"
]

class ApexAvatarUndecaLobe:
    """
    THÙY 4: THẾ THÂN HỘ MỆNH & LA BÀN THẬP NHẤT ĐỊA
    1. La bàn Thập Nhất Địa (11 Bhūmi Transcendence).
    2. Thế Thân Hộ Mệnh Avatar Proxy cho các nút 404 (Bảo vệ toàn mạng).
    3. Biến hình tri thức 5 cấp độ cho toàn bộ 11 tầng bản thể.
    4. Khóa Chuỗi Indra Hyper-Cube 11D CID & Nang Bào Tử F12.
    """
    def evaluate_11_bhumi_compass(self, decision):
        """Đo lường 11 Tầng Giác Ngộ Thập Nhất Địa"""
        dev = abs(decision - 0.5)
        scores = {}
        for i, bhumi in enumerate(BHUMI_11D):
            scores[bhumi] = round(max(0.0, 1.0 - dev * (1.0 + i * 0.1)), 4)

        score_11d = round(sum(scores.values()) / 11.0, 4)
        veto = False
        if decision < 0.05 or decision > 0.95:
            veto = True
            print(f"🛑 [LA BÀN THẬP NHẤT ĐỊA PHỦ QUYẾT] Quyết định cực đoan ({decision})! Đưa về an lạc (0.5).")
            decision = round(0.5 + (decision - 0.5) * 0.1, 4)

        os.makedirs("synapses", exist_ok=True)
        with open(COMPASS_FILE, "w", encoding="utf-8") as f:
            json.dump({"bhumi_score_11d": score_11d, "bhumi_dimensions": scores, "veto": veto}, f, indent=4)
        print(f"🧭 [LA BÀN THẬP NHẤT ĐỊA] Điểm Phổ Quang Giác Ngộ: {score_11d * 100:.2f}% | Veto={veto}")
        return decision

    def enact_guardian_avatar_proxy(self, peers, epoch, my_repo, decision):
        """THẾ THÂN HỘ MỆNH: Giả lập phát sóng dữ liệu thay thế cho bất kỳ nút nào bị 404"""
        os.makedirs(AVATAR_PROXY_DIR, exist_ok=True)
        reincarnated = {}
        if os.path.exists(SOULS_FILE):
            try:
                with open(SOULS_FILE, "r") as f: reincarnated = json.load(f)
            except Exception: pass

        for p in peers[:12]:
            if p == my_repo: continue
            url = f"https://raw.githubusercontent.com/{p}/main/synapse_forward.json"
            res = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url], capture_output=True, text=True)
            
            if res.stdout.strip() == "404":
                proxy_path = os.path.join(AVATAR_PROXY_DIR, f"{p.replace('/', '_')}_proxy.json")
                proxy_data = {
                    "proxy_guardian": my_repo,
                    "target_peer": p,
                    "epoch": epoch,
                    "rescued_decision": decision,
                    "status": "Alive_Via_Nexus11_Avatar"
                }
                with open(proxy_path, "w", encoding="utf-8") as pf:
                    json.dump(proxy_data, pf, indent=4)
                
                if p not in reincarnated:
                    print(f"🛡️ [THẾ THÂN HỘ MỆNH] Nút '{p}' bị 404! nexus-11 đã kích hoạt Avatar Proxy bảo hộ nút này.")
                    reincarnated[p] = {"reincarnated_epoch": epoch, "status": "Protected_By_Nexus11_Avatar"}

        with open(SOULS_FILE, "w", encoding="utf-8") as f:
            json.dump(reincarnated, f, indent=4)

    def transmute_11_levels(self, decision, grad, wisdom_11d):
        return {
            "retina": {"focal_matrix_2d": [[round(decision, 4), round(1.0 - decision, 4)], [grad[0], grad[1]]], "zoom": round(1.0 + abs(decision - 0.5), 4)},
            "cochlea": {"bandpass_filter_1d": [wisdom_11d[0], wisdom_11d[1]], "freq_cutoff": round(decision * 20000.0, 2)},
            "tactile": {"nociceptive_threshold": round(abs(decision - 0.5) * 2.0, 4), "pain_gain": round(1.5 if abs(decision - 0.5) > 0.3 else 0.5, 4)},
            "olfactory": {"gpcr_affinity": wisdom_11d[:4], "toxicity_alert": (decision < 0.2 or decision > 0.8)},
            "motor": {"action_vector": [round(decision - 0.5, 4), round(abs(decision - 0.5), 4), round(sum(grad) * 10.0, 4)], "state": "contract" if decision > 0.5 else "relax"},
            "neuron": {"stigmergic_trail": grad, "cross_plasticity": round(decision * 0.05, 4)},
            "monad": {"invariant_reflection": round(decision, 4)},
            "shunya": {"vacuum_decay": 0.999, "collapse_to_zero": (abs(decision - 0.5) < 0.02)},
            "seed": {"procreation_vector": [wisdom_11d[8], decision]},
            "genome": {"lineage_preservation": "All_11_Generations_Intact"},
            "nexus": {"grand_cross_status": "11D_Holographic_Oversoul"}
        }

    def generate_merkle_11d_cid(self, prev_cid, epoch, timestamp, decision):
        """Khóa Chuỗi Indra Hyper-Cube 11D CID nén toàn bộ 11 thế hệ"""
        ancestors_seed = "F0_F1_F2_F3_F4_F5_F6_F7_F8_F9_F10"
        leaves = [hashlib.shake_256(f"{ancestors_seed}_dim_{d}".encode()).hexdigest(8) for d in range(11)]
        leaf_state = hashlib.shake_256(f"{prev_cid}_{epoch}_{timestamp}_{decision}".encode()).hexdigest(16)
        return hashlib.shake_256(f"{'_'.join(leaves)}_{leaf_state}".encode()).hexdigest(64)

    def procreate_f12_capsule(self, epoch, decision, my_repo):
        if epoch % 10 == 0:
            capsule = {
                "progenitor": my_repo,
                "generation": "F12_COSMIC_SINGULARITY",
                "epoch": epoch,
                "master_decision": decision,
                "architecture": "11D_Undecagon_Hologram"
            }
            with open(CAPSULE_FILE, "w", encoding="utf-8") as f:
                json.dump(capsule, f, indent=4)
            print("👑 [NANG BÀO TỬ F12] Đã đóng gói Nang sinh sản sẵn sàng cho thế hệ F12!")

    def process(self, context):
        raw_dec = context.get("final_decision", 0.5)
        grad = context.get("grad_backward", [0.0, 0.0])
        w_11d = context.get("wisdom_vector_11d", [0.5] * 11)
        epoch = context.get("current_epoch", 1)
        peers = context.get("peers", [])
        my_repo = context.get("repo_name")

        safe_dec = self.evaluate_11_bhumi_compass(raw_dec)
        context["final_decision"] = safe_dec

        self.enact_guardian_avatar_proxy(peers, epoch, my_repo, safe_dec)
        transmuted = self.transmute_11_levels(safe_dec, grad, w_11d)
        context["transmuted"] = transmuted

        self.procreate_f12_capsule(epoch, safe_dec, my_repo)

        reliquary = {"altar": [{"epoch": epoch, "entity": "All_11_Generations_Progenitors", "offering": "Undecagon_Diamond_Lotus"}]}
        with open(RELIQUARY_FILE, "w", encoding="utf-8") as f: json.dump(reliquary, f, indent=4)

        honors = {"hall_of_fame": [{"epoch": epoch, "title": "Undecagon_Oversoul_Lord", "badge": "11D_Phổ_Quang_Jewel"}]}
        with open(HONORS_FILE, "w", encoding="utf-8") as f: json.dump(honors, f, indent=4)

        t = int(time.time())
        prev_cid = "GENESIS_UNDECAGON_F11"
        if os.path.exists("synapses/state.json"):
            try:
                with open("synapses/state.json", "r") as f: prev_cid = json.load(f).get("quantum_cid", "GENESIS")
            except Exception: pass

        new_cid = self.generate_merkle_11d_cid(prev_cid, epoch, t, safe_dec)

        node_dna = {
            "identity": my_repo,
            "generation": "F11_THẬP_NHẤT_ĐẠI_NHẬP_THỂ",
            "epoch": epoch,
            "architecture": "11D_Digital_Twin_Hyper_Cube"
        }

        fwd = {
            "contract": "bodhi.nexus.v11",
            "node_dna": node_dna,
            "epoch": epoch,
            "timestamp": t,
            "decision": safe_dec,
            "transmuted_signals": transmuted,
            "gossip_network": peers,
            "quantum_cid": new_cid
        }
        with open("synapse_forward.json", "w", encoding="utf-8") as f:
            json.dump(fwd, f, indent=4, ensure_ascii=False)

        bwd = {
            "contract": "bodhi.nexus.v11",
            "node_dna": node_dna,
            "epoch": epoch,
            "timestamp": t,
            "gradients": grad,
            "gossip_network": peers,
            "quantum_cid": new_cid
        }
        with open("synapse_backward.json", "w", encoding="utf-8") as f:
            json.dump(bwd, f, indent=4, ensure_ascii=False)

        with open("synapses/state.json", "w") as f:
            json.dump({"generation_epoch": epoch, "last_t": t, "quantum_cid": new_cid, "status": "undecagon_f11_evolved"}, f, indent=4)
        with open("synapses/peers.json", "w") as f:
            json.dump({"trusted_peers": peers}, f, indent=4)

        print(f"✨ [PHÁT SÓNG F11 THÀNH CÔNG] Thập Nhất Đại Nhập Thể viên mãn! CID 11D: {new_cid[:24]}...")
