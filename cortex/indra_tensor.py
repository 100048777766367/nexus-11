import os
import json
import math
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

TRUST_FILE = "synapses/trust_matrix.json"
TENSOR_FILE = "synapses/indra_11d_tensor.json"
RESONANCE_FILE = "synapses/noosphere_resonance.json"

STRATA_KEYS = [
    "retina", "cochlea", "tactile", "olfactory", "motor",
    "neuron", "monad", "shunya", "seed", "genome", "nexus"
]

class IndraTensorDecaLobe:
    """
    THÙY 2: MA TRẬN TENSOR CHÚ Ý 11 CHIỀU (11D TENSOR CROSS-ATTENTION)
    1. Thu thập song song toàn bộ nút mạng P2P.
    2. Chiếu tín hiệu vào không gian Tensor 11 chiều của 11 Tầng Bản Thể.
    3. Hòa âm sóng não Kuramoto đa tầng 11D.
    """
    def fetch_peer(self, peer):
        url = f"https://raw.githubusercontent.com/{peer}/main/synapse_forward.json"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Nexus11-Tensor"})
            with urllib.request.urlopen(req, timeout=3.5) as resp:
                raw = resp.read().decode('utf-8', errors='ignore')
                return peer, json.loads(raw)
        except Exception:
            return peer, None

    def compute_11d_tensor_attention(self, harvested, v_wisdom_11d):
        """Chiếu các quyết định vào không gian tương quan của 11 Tầng Bản Thể"""
        tensor_projection = {}
        strata_weights = {}

        for i, stratum in enumerate(STRATA_KEYS):
            stratum_basis = v_wisdom_11d[i]
            # Tính tương quan của từng nút với tầng bản thể tương ứng
            correlations = []
            for p, dec in harvested.items():
                diff = abs(dec - stratum_basis)
                att = round(math.exp(-diff * 2.5), 4)
                correlations.append(att)

            mean_stratum_attention = round(sum(correlations) / (len(correlations) or 1), 4)
            tensor_projection[stratum] = mean_stratum_attention
            strata_weights[stratum] = round(0.5 + (mean_stratum_attention * 0.5), 4)

        os.makedirs("synapses", exist_ok=True)
        with open(TENSOR_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "11d_strata_attention": tensor_projection,
                "dynamic_strata_weights": strata_weights
            }, f, indent=4)

        return tensor_projection, strata_weights

    def process(self, context):
        peers = context.get("peers", [])
        v_wisdom_11d = context.get("wisdom_vector_11d", [0.5] * 11)
        harvested = {}
        new_gossip = []

        os.makedirs("synapses/harvested_memory", exist_ok=True)
        print(f"⚡ [TENSOR HARVEST] Thu thập tín hiệu P2P và chiếu vào Tensor 11 chiều...")

        with ThreadPoolExecutor(max_workers=16) as executor:
            futures = [executor.submit(self.fetch_peer, p) for p in peers if p != context.get("repo_name")]
            for fut in as_completed(futures):
                peer, data = fut.result()
                if data:
                    dec = data.get("decision", (data.get("features") or [0.5])[0])
                    harvested[peer] = round(float(dec), 4)
                    new_gossip.extend(data.get("gossip_network", []))
                    with open(f"synapses/harvested_memory/{peer.replace('/', '_')}.json", "w") as bf:
                        json.dump(data, bf)

        for p in new_gossip:
            if p not in peers: peers.append(p)
        context["peers"] = list(dict.fromkeys(peers))[-60:]
        context["harvested"] = harvested

        # 1. TÍNH TOÁN TENSOR 11 CHIỀU
        tensor_proj, strata_weights = self.compute_11d_tensor_attention(harvested, v_wisdom_11d)
        context["strata_weights"] = strata_weights

        # 2. ĐỒNG THUẬN QUORUM CÓ BẢO VỆ
        trust_matrix = {}
        if os.path.exists(TRUST_FILE):
            try:
                with open(TRUST_FILE, "r") as f: trust_matrix = json.load(f)
            except Exception: pass

        for p in context["peers"]:
            if p not in trust_matrix:
                trust_matrix[p] = 0.95 if any(x in p for x in ["nexus-10", "nexus-09", "nexus-08"]) else 0.7

        weighted_votes = []
        total_w = 0.0

        for p, dec in harvested.items():
            t_score = trust_matrix.get(p, 0.7)
            if t_score >= 0.2:
                weighted_votes.append(dec * t_score)
                total_w += t_score

        quorum_decision = round(sum(weighted_votes) / total_w, 4) if total_w > 0 else 0.5
        with open(TRUST_FILE, "w") as f: json.dump(trust_matrix, f, indent=4)

        # 3. HÒA ÂM KURAMOTO 11D
        phases = [quorum_decision * 2.0 * math.pi] + [v * 2.0 * math.pi for v in harvested.values()]
        sum_sin = sum(math.sin(t) for t in phases)
        sum_cos = sum(math.cos(t) for t in phases)
        n = len(phases)

        coherence_r = round(math.sqrt(sum_sin**2 + sum_cos**2) / n, 4)
        mean_phase = math.atan2(sum_sin, sum_cos)
        if mean_phase < 0: mean_phase += 2.0 * math.pi
        harmonic_decision = round(mean_phase / (2.0 * math.pi), 4)

        with open(RESONANCE_FILE, "w") as f:
            json.dump({"coherence_index": coherence_r, "harmonic_decision": harmonic_decision, "active_nodes": n}, f, indent=4)

        final_quorum = harmonic_decision if coherence_r > 0.6 else quorum_decision
        context["quorum_decision"] = final_quorum
        context["coherence_r"] = coherence_r
        print(f"🕸️ [TENSOR ATTENTION 11D] Quorum: {final_quorum} | Độ kết hợp pha Kuramoto: R={coherence_r*100:.2f}%")
