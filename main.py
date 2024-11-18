class Node:
    def __init__(self, question, yes_node=None, no_node=None, hasil=None):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node
        self.hasil = hasil


    def build_tree():
        node18 = Node(None, hasil="Mohon maaf untuk genre game hanya sebatas itu")

        # Hasil akhir spesifikasi untuk setiap simpul akhir
        node17 = Node(None, hasil="Rekomendasi PC Entry-Level (<4 juta):\nProcessor: Intel Core i3-10100K\nRAM: 8GB DDR4 2666 MHz\nStorage: SSD SATA 256GB\nPSU: 400W 80+ Bronze\nVGA: Integrated Graphics (Intel UHD).")
        node16 = Node(None, hasil="Rekomendasi PC Entry-Level (<4 juta):\nProcessor: AMD Athlon 3000G\nRAM: 8GB DDR4 2666 MHz\nStorage: SSD SATA 256GB\nPSU: 400W 80+ Bronze\nVGA: Integrated Graphics (AMD Vega 3).")
        node15 = Node(None, hasil="Rekomendasi PC Mid-End (8-15 juta):\nProcessor: Intel Core i5-13400F\nRAM: 16GB DDR4 3200 MHz\nVGA: NVIDIA RTX 3050\nStorage: SSD NVMe 512GB")
        node14 = Node(None, hasil="Rekomendasi PC Mid-End (8-15 juta):\nProcessor: AMD Ryzen 5 5600\nRAM: 16GB DDR4 3200 MHz\nVGA: AMD RX 6600\nStorage: SSD NVMe 512GB")
        node13 = Node(None, hasil="Rekomendasi PC High-End (>15 juta):\nProcessor: Intel Core i7-13700F\nRAM: 32GB DDR5 5600 MHz\nVGA: NVIDIA RTX 4070\nStorage: SSD NVMe 1TB + HDD 2TB")
        node12 = Node(None, hasil="Rekomendasi PC High-End (>15 juta):\nProcessor: AMD Ryzen 7 7800X3D\nRAM: 32GB DDR5 6000 MHz\nVGA: AMD RX 7800 XT\nStorage: SSD NVMe 1TB + HDD 2TB")
        node11 = Node(None, hasil="Kalo miskin jangan rakit PC, anjing")
        
        # Bangun simpul dari bawah ke atas
        node9 = Node("Apakah anda ingin menggunakan processor Ryzen?", yes_node=node16, no_node=node17)
        node10 = Node("Apakah anda ingin menggunakan processor INTEL?", yes_node=node17, no_node=node16)

        node7 = Node("Apakah anda ingin menggunakan processor AMD?", yes_node=node14, no_node=node15)
        node8 = Node("Apakah anda ingin menggunakan processor INTEL?", yes_node=node15, no_node=node14)

        node5 = Node("Apakah anda ingin menggunakan processor AMD?", yes_node=node12, no_node=node13)
        node6 = Node("Apakah anda ingin menggunakan processor INTEL?", yes_node=node13, no_node=node12)

        node4 = Node("Apakah budget Anda di bawah 8 juta?", yes_node=node9, no_node=node11)
        node3 = Node("Apakah budget Anda antara 8-15 juta?", yes_node=node7, no_node=node4)
        node2 = Node("Apakah budget Anda di atas 15 juta?", yes_node=node5, no_node=node3)
        node1 = Node("Apakah Anda suka bermain game genre eSport?", yes_node=node2, no_node=node18)
        node0 = Node("Apakah Anda suka bermain game genre OpenWorld atau RPG?", yes_node=node2, no_node=node1)
        nodemin1 = Node("Apakah Anda suka bermain game genre Casual?", yes_node=node17, no_node=node0)
        nodemin2 = Node("Apakah anda merakit pc untuk produktivitas ?", yes_node=node2, no_node=node)
        
        return nodemin1

    def inferensia(node):
        while node.question:  # Selama masih ada pertanyaan
            jawaban = input(node.question + " (yes/no): ").lower()
            if jawaban == "yes":
                node = node.yes_node
            elif jawaban == "no":
                node = node.no_node
            else:
                print("Saya tidak mengerti, coba ketik 'yes' atau 'no'.")
        print("Rakit PC:\n", node.hasil)


# Main program
if __name__ == "__main__":
    decision_tree = Node.build_tree()
    Node.inferensia(decision_tree)
