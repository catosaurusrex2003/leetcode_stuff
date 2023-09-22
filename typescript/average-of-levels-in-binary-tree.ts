class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function averageOfLevels(root: TreeNode | null): number[] {
    let final: number[] = [];
    if (root == null) return [];
    let queue: TreeNode[] = [root];
    while (queue.length > 0) {
        let avg: number = 0;
        const size = queue.length;
        for (let i = 0; i < size; i++) {
            console.log(queue[0].val)
            avg += queue[0].val;
            if (queue[0].left !== null) { queue.push(queue[0].left!) }
            if (queue[0].right !== null) { queue.push(queue[0].right!) }
            queue.shift()
        }
        final.push(avg / size)
    }
    return final
};