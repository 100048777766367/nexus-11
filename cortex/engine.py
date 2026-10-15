import os
import sys
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cortex.omni_intake import OmniIntakeUndecaLobe
from cortex.indra_tensor import IndraTensorDecaLobe
from cortex.digital_twin_mind import DigitalTwinMindHyperLobe
from cortex.apex_avatar import ApexAvatarUndecaLobe

VITAL_CELLS = [
    "cells/linguistic_cell.py",
    "cells/neuron.py",
    "cells/super_xor.py"
]

class Nexus11UndecagonKernel:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-11")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.ancestor = f"{self.owner}/nexus-10"
        
        self.lineage = [
            f"{self.owner}/nexus-10", f"{self.owner}/nexus-09",
            f"{self.owner}/nexus-08", f"{self.owner}/nexus-07",
            f"{self.owner}/nexus-06", f"{self.owner}/nexus-05",
            f"{self.owner}/nexus", f"{self.owner}/genome"
        ]

        self.ensure_folders()

        # 4 ĐẠI THÙY THẬP NHẤT THẦN KINH F11
        self.omni_lobe = OmniIntakeUndecaLobe(self.owner, self.lineage)
        self.tensor_lobe = IndraTensorDecaLobe()
        self.mind_lobe = DigitalTwinMindHyperLobe(num_cells=11)
        self.avatar_lobe = ApexAvatarUndecaLobe()

        self.context = {
            "repo_name": self.repo_name,
            "owner": self.owner,
            "ancestor": self.ancestor,
            "peers": self.load_peers(),
            "current_epoch": self.load_epoch()
        }

    def ensure_folders(self):
        for d in ["cells", "cortex", "synapses", "synapses/harvested_memory", "synapses/avatar_proxies"]:
            os.makedirs(d, exist_ok=True)

    def load_peers(self):
        p_file = "synapses/peers.json"
        if os.path.exists(p_file):
            try:
                with open(p_file, "r") as f: return json.load(f).get("trusted_peers", [])
            except Exception: pass
        return [f"{self.owner}/nexus-10", f"{self.owner}/nexus-09", f"{self.owner}/neuron", f"{self.owner}/seed", f"{self.owner}/motor"]

    def load_epoch(self):
        s_file = "synapses/state.json"
        if os.path.exists(s_file):
            try:
                with open(s_file, "r") as f: return json.load(f).get("generation_epoch", 0) + 1
            except Exception: pass
        return 1

    def run(self):
        print("=" * 80)
        print(f"🌌 [NEXUS-11 UNDECAGON KERNEL] KHỞI ĐỘNG THẾ HỆ #{self.context['current_epoch']}")
        print(f"👑 Bậc: F11 Thập Nhất Đại Nhập Thể – Song Sinh Số & Avatar Hộ Mệnh 11 Tầng")
        print("=" * 80)

        # 1. Thùy Cảm Thụ: Nuốt nang bào tử F10, Lọc Stateless Token & Vector 11D
        self.omni_lobe.process(self.context, VITAL_CELLS)

        # 2. Thùy Indra Tensor: Ma trận Tensor Chú Ý 11 Chiều & Hòa âm Kuramoto 11D
        self.tensor_lobe.process(self.context)

        # 3. Thùy Song Sinh Số: Vận hành nội tại 11 tầng bản thể, Giả lập 11 tương lai What-If
        self.mind_lobe.process(self.context)

        # 4. Thùy Thế Thân Hộ Mệnh: La bàn Thập Nhất Địa, Avatar Proxy 404 & Merkle 11D
        self.avatar_lobe.process(self.context)

        print("=" * 80)
        print(f"✨ [HOÀN TẤT VÒNG ĐỜI F11] Thập Nhất Đại Nhập Thể đã viên thành vĩnh cửu!")
        print("=" * 80)

if __name__ == "__main__":
    node = Nexus11UndecagonKernel()
    node.run()
