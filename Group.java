public class Group {
    private char name;
    private int weight;
    private int members;
    private double profit;

    public Group() {
        this.name = 'X';
        this.weight = 0;
        this.members = 0;
        this.profit = 0;
    }

    public Group(char someName, int someWeight, int someMembers) {
        this.name = someName;
        this.weight = someWeight;
        this.members = someMembers;
        this.profit = (this.weight-100)*5;
    }

    public char getName() {
        return this.name;
    }

    public int getWeight() {
        return this.weight;
    }

    public int getMembers() {
        return this.members;
    }

    public double getProfit() {
        return this.profit;
    }

    public void setName(char someName) {
        this.name = someName;
    }

    public void setWeight(int someWeight) {
        this.weight = someWeight;
    }

    public void setMembers(int someMembers) {
        this.members = someMembers;
    }

    public void setProfit(double someProfit) {
        this.profit = someProfit;
    }
}
