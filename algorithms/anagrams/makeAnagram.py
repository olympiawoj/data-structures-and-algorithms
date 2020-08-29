# I Implemented the same using HashMaps in Java. But then i came across this solution. Its nice. so implemented the same in java.

# public static int numberNeededAr(String a,String b) {
#         int[] af = new int[26];
#         int ops = 0;
#         for(int i = 0; i < a.length(); ++i) af[a.charAt(i) - 'a']++;
#         for(int i = 0; i < b.length(); ++i) af[b.charAt(i) - 'a']--;
#         for (int anAf : af) ops += Math.abs(anAf);
#         return ops;
#     }