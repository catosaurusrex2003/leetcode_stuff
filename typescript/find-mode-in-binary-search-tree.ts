class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
      this.val = val === undefined ? 0 : val;
      this.left = left === undefined ? null : left;
      this.right = right === undefined ? null : right;
    }
  }
  
  const findMode = (root: TreeNode): number[] => {
    const queue = [root];
    let track = new Map<number, number>();
    let highest: { count: number; elements: number[] } = {
      count: 0,
      elements: [],
    };
    while (queue.length) {
      // const { val, left, right } = queue.shift() as TreeNode;
      const currNode = queue.shift();
      if (!currNode) continue;
      const { val, left, right } = currNode;
      const currCount = (track.get(val) ?? 0) + 1;
      track.set(val, currCount);
      if (currCount > highest.count) {
        highest = {
          count: currCount,
          elements: [],
        };
      }
      if (currCount == highest.count) {
        highest = {
          count: currCount,
          elements: [...highest.elements, val],
        };
      }
      queue.push(left as TreeNode);
      queue.push(right as TreeNode);
    }
    return highest.elements;
  };
  