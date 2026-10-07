import java.util.Arrays;
import java.util.Scanner;

class Edge {
    int u;
    int v;
    int w;

    Edge(int u, int v, int w) {
        this.u = u;
        this.v = v;
        this.w = w;
    }
}

public class Main {
    static int[] parent = new int[1010];  // polje roditelja (DSU)
    static int m, n, k;  // n je broj vrhova, m broj bridova, k traženi broj šećernih vuna

    static Edge[] edges = new Edge[10010];
    static int l;

    static void addEdge(int u, int v, int w) {
        edges[++l] = new Edge(u, v, w);
    }

    // standardni DSU (union-find)
    static int findroot(int x) {
        if (parent[x] != x) {
            parent[x] = findroot(parent[x]);
        }
        return parent[x];
    }

    static void Merge(int x, int y) {
        x = findroot(x);
        y = findroot(y);
        parent[x] = y;
    }

    static boolean cmp(Edge A, Edge B) {
        return A.w < B.w;
    }

    // Kruskalov algoritam
    static void kruskal() {
        int tot = 0;  // broj odabranih bridova
        int ans = 0;  // ukupni trošak

        for (int i = 1; i <= m; i++) {
            int xr = findroot(edges[i].u);
            int yr = findroot(edges[i].v);
            if (xr != yr) {   // ako su predstavnici različiti
                Merge(xr, yr); // spoji
                tot++; // još jedan brid
                ans += edges[i].w; // dodaj trošak
                if (tot == n - k) {  // provjeri daje li broj odabranih bridova k šećernih vuna
                    System.out.println(ans);
                    return;
                }
            }
        }
        System.out.println("No Answer");  // ne može se povezati
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        k = scanner.nextInt();

        if (n == k) { // poseban rubni slučaj
            System.out.println("0");
            return;
        }

        // inicijalizacija
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }
        for (int i = 1; i <= m; i++) {
            int u = scanner.nextInt();
            int v = scanner.nextInt();
            int w = scanner.nextInt();
            addEdge(u, v, w);  // dodaj brid
        }
        Arrays.sort(edges, 1, m + 1, (a, b) -> Integer.compare(a.w, b.w));  // prvo sortiraj po težini brida
        kruskal();
        scanner.close();
    }
}
