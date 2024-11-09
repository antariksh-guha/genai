// src/utils/jsonHelpers.ts
export const validateJson = (text: string): boolean => {
  try {
    JSON.parse(text);
    return true;
  } catch {
    return false;
  }
};

export const formatJobDescription = (text: string): string => {
  return JSON.stringify(
    {
      title: "",
      level: "",
      department: "",
      requirements: [],
    },
    null,
    2
  );
};
