from collections import defaultdict

def rrf_fuse(rankings, k=60):
    scores = defaultdict(float)
    for rk in rankings:
        for pos, doc_id in enumerate(rk, start=1): scores[doc_id] += 1.0 / (k + pos)
    return sorted(scores, key=lambda d: scores[d], reverse=True)

if __name__ == "__main__":
    assert rrf_fuse([["d1", "d2"], ["d2", "d3"]])[0] == "d2"
    print("[PASS] 083_rrf_hybrid_fusion")
